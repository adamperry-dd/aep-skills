# Wanda: Pruning by Weights and Activations

Based on ICLR 2024 paper (arXiv 2306.11695) - A Simple and Effective Pruning Approach for Large Language Models

**GitHub**: https://github.com/locuslab/wanda

## Core Innovation

### Pruning Criterion

**Key insight**: Weight importance = magnitude × usage

```python
importance(w_ij) = |w_ij| × ||X_i||

where:
- w_ij: Weight connecting input i to output j
- X_i: Input activation norm for dimension i
```

**Why better than magnitude pruning**:
```
Weight A: magnitude=0.5, activation=0.1 → importance=0.05
Weight B: magnitude=0.3, activation=0.8 → importance=0.24

Magnitude pruning: Keeps A (larger weight)
Wanda: Keeps B (more important overall) ✓
```

## Complete Algorithm

```python
import torch
from transformers import AutoModelForCausalLM

def wanda_prune(model, calib_data, sparsity=0.5):
    """
    Wanda pruning algorithm.

    Steps:
    1. Collect activation statistics on calibration data
    2. Compute importance = |weight| × activation
    3. Prune lowest importance weights per output dimension
    """
    activations = {}

    def activation_hook(name):
        def hook(module, input, output):
            X = input[0].detach()
            act_norm = X.abs().mean(dim=0)  # Per-input-dimension norm
            if name in activations:
                activations[name] += act_norm
            else:
                activations[name] = act_norm
        return hook

    # Register hooks
    hooks = []
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Linear):
            hook = module.register_forward_hook(activation_hook(name))
            hooks.append(hook)

    # Run calibration
    model.eval()
    with torch.no_grad():
        for batch in calib_data:
            model(**batch)

    # Remove hooks
    for hook in hooks:
        hook.remove()

    # Prune based on importance (per-output dimension)
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Linear) and name in activations:
            W = module.weight.data
            act = activations[name]

            # Importance matrix
            importance = W.abs() * act.unsqueeze(0)  # (out_features, in_features)

            # Per-output pruning (ensures balanced capacity)
            for out_dim in range(W.size(0)):
                importance_out = importance[out_dim, :]
                threshold = torch.quantile(importance_out, sparsity)
                mask = importance_out >= threshold
                W[out_dim, :] *= mask.float()

    return model
```

## Calibration Data

### Requirements

- **Amount**: 128 samples (from paper)
- **Source**: Any text corpus (C4, WikiText, etc.)
- **Length**: 2048 tokens per sample

```python
from datasets import load_dataset

calib_dataset = load_dataset("allenai/c4", "en", split="train", streaming=True)
calib_samples = []

for i, example in enumerate(calib_dataset):
    if i >= 128:
        break
    text = example['text'][:2048]
    calib_samples.append(text)

tokenized = tokenizer(
    calib_samples,
    return_tensors="pt",
    padding=True,
    truncation=True,
    max_length=2048
)
```

**Quality note**: Higher-quality calibration data → slightly better pruning (but not critical).

## Performance Results

### Unstructured Sparsity

**From ICLR 2024 paper** (LLaMA models on zero-shot tasks):

| Model | Sparsity | Method | Perplexity (WikiText2) | Avg Accuracy |
|-------|----------|--------|------------------------|--------------|
| LLaMA-7B | 0% | Baseline | 5.68 | 60.2% |
| LLaMA-7B | 50% | Magnitude | 8.45 | 55.3% (-4.9%) |
| LLaMA-7B | 50% | SparseGPT | 6.32 | 59.1% (-1.1%) |
| LLaMA-7B | 50% | **Wanda** | **6.18** | **59.4% (-0.8%)** |

**Key finding**: Wanda achieves near-SparseGPT quality with simpler algorithm (no Hessian).

### Scaling to Large Models

| Model Size | Sparsity | Wanda PPL | Degradation |
|------------|----------|-----------|-------------|
| LLaMA-7B | 50% | 6.18 | +0.50 |
| LLaMA-13B | 50% | 5.42 | +0.38 |
| LLaMA-30B | 50% | 4.77 | +0.21 |
| LLaMA-65B | 50% | 4.25 | +0.15 |

**Scaling behavior**: Larger models → better pruning (more redundancy).

## Practical Deployment

### Using Official Wanda Script

```bash
# Clone repo
git clone https://github.com/locuslab/wanda
cd wanda

# Prune LLaMA-7B to 50% sparsity
python main.py \
    --model meta-llama/Llama-2-7b-hf \
    --prune_method wanda \
    --sparsity_ratio 0.5 \
    --sparsity_type unstructured \
    --save ./pruned_models/llama-7b-wanda-50

# Evaluate
python eval.py \
    --model ./pruned_models/llama-7b-wanda-50 \
    --tasks arc_easy,hellaswag,winogrande
```

### Custom Integration

```python
from transformers import pipeline

# Load pruned model
model = AutoModelForCausalLM.from_pretrained("./pruned_models/llama-7b-wanda-50")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")

# Use normally
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
output = pipe("Once upon a time", max_new_tokens=100)
```

## Wanda with N:M Sparsity

See [nm-sparsity.md](nm-sparsity.md) for N:M implementation details.

Quick example:
```python
def wanda_nm_prune(model, calib_data, n=2, m=4):
    """Wanda with N:M structured sparsity for hardware acceleration."""
    activations = collect_activations(model, calib_data)
    
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Linear):
            W = module.weight.data
            act = activations[name]
            importance = W.abs() * act.unsqueeze(0)
            W.data = apply_nm_mask(W, importance, n=n, m=m)
    
    return model
```

## Comparison with SparseGPT

| Aspect | Wanda | SparseGPT |
|--------|-------|-----------|
| Complexity | O(n) per layer | O(n²) per layer |
| Speed | Fast (~minutes) | Slow (~hours) |
| Memory | Low (activations) | High (Hessian) |
| Quality (50%) | -0.8% accuracy | -0.4% accuracy |
| Implementation | Simple (~100 lines) | Complex (matrix inverse) |

**Recommendation**: Use Wanda unless you need absolute best quality.

## Limitations

1. **No retraining**: One-shot only (can't recover from bad pruning)
2. **Activation dependency**: Requires calibration data
3. **Unstructured sparsity**: No speedup without specialized hardware (unless using N:M)

## Resources

- Paper: https://arxiv.org/abs/2306.11695
- GitHub: https://github.com/locuslab/wanda
- ICLR 2024: https://openreview.net/forum?id=PxoFut3dWW
