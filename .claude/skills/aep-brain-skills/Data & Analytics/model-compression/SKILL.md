---
name: model-compression
description: Compress large language models using pruning (Wanda, SparseGPT, N:M sparsity) and knowledge distillation (MiniLLM, temperature scaling, soft targets). Use when: (1) reducing model size 40-60% with <1% accuracy loss, (2) accelerating inference 2-4× with hardware-friendly sparsity, (3) transferring GPT-4/70B capabilities to smaller open-source models, (4) deploying on constrained hardware (mobile, edge), (5) reducing inference costs via smaller models, (6) compressing without retraining using one-shot methods, (7) creating specialized models via distillation. Covers unstructured pruning, structured pruning, N:M sparsity, magnitude pruning, reverse KLD, logit distillation, temperature scaling, and combined compression strategies. Key papers: Wanda ICLR 2024 (arXiv 2306.11695), SparseGPT (arXiv 2301.00774), MiniLLM (arXiv 2306.08543), Hinton et al. 2015 (arXiv 1503.02531).
---

# Model Compression: Pruning + Distillation

Reduce LLM size, cost, and latency using pruning (remove weights) and distillation (transfer knowledge from large to small models).

## When to Read Additional References

**Pruning Methods** (remove weights):
- **Wanda pruning**: See [wanda-pruning.md](references/wanda-pruning.md) when using activation-based importance scoring for one-shot pruning with <1% accuracy loss at 50% sparsity
- **SparseGPT**: See [sparsegpt-pruning.md](references/sparsegpt-pruning.md) when quality is critical and you can afford second-order Hessian computation for near-lossless pruning
- **N:M sparsity**: See [nm-sparsity.md](references/nm-sparsity.md) when deploying to NVIDIA GPUs with sparse tensor cores for 2× hardware speedup

**Distillation Methods** (transfer knowledge):
- **MiniLLM (Reverse KLD)**: See [minillm-distillation.md](references/minillm-distillation.md) when distilling for generative tasks requiring diverse outputs and mode-covering behavior
- **Standard distillation**: See [standard-distillation.md](references/standard-distillation.md) when using temperature scaling and soft targets for basic teacher-student training

**Advanced Topics**:
- **Combined strategies**: See [advanced-strategies.md](references/advanced-strategies.md) when combining pruning + distillation, gradual pruning, layer-wise strategies, or multi-teacher approaches
- **Evaluation & benchmarks**: See [evaluation-benchmarks.md](references/evaluation-benchmarks.md) when comparing methods or validating compression quality

## Quick Start

### Pruning: Wanda (One-Shot, No Retraining)

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-hf",
    torch_dtype=torch.float16,
    device_map="cuda"
)
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")

# Calibration data
calib_data = [
    "The quick brown fox jumps over the lazy dog.",
    "Machine learning is transforming the world.",
]

def wanda_prune(model, calib_data, sparsity=0.5):
    """Prune by weight magnitude × input activation."""
    activations = {}
    
    # Collect activation statistics
    def hook_fn(name):
        def hook(module, input, output):
            activations[name] = input[0].detach().abs().mean(dim=0)
        return hook
    
    hooks = []
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Linear):
            hooks.append(module.register_forward_hook(hook_fn(name)))
    
    model.eval()
    with torch.no_grad():
        for text in calib_data:
            inputs = tokenizer(text, return_tensors="pt").to(model.device)
            model(**inputs)
    
    for hook in hooks:
        hook.remove()
    
    # Prune based on importance
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Linear) and name in activations:
            W = module.weight.data
            act = activations[name]
            importance = W.abs() * act.unsqueeze(0)
            threshold = torch.quantile(importance.flatten(), sparsity)
            mask = importance >= threshold
            W *= mask.float()
    
    return model

# Apply 50% sparsity
pruned_model = wanda_prune(model, calib_data, sparsity=0.5)
pruned_model.save_pretrained("./llama-2-7b-wanda-50")
```

### Distillation: Basic Teacher-Student

```python
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, Trainer, TrainingArguments

# Load models
teacher = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-70b-hf",
    torch_dtype=torch.float16,
    device_map="auto"
)
student = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-hf",
    torch_dtype=torch.float16
)

def distillation_loss(student_logits, teacher_logits, labels, temperature=2.0, alpha=0.7):
    """Combine soft (KLD) and hard (CE) losses."""
    # Hard loss
    hard_loss = F.cross_entropy(
        student_logits.view(-1, student_logits.size(-1)),
        labels.view(-1)
    )
    
    # Soft loss
    soft_targets = F.softmax(teacher_logits / temperature, dim=-1)
    soft_student = F.log_softmax(student_logits / temperature, dim=-1)
    soft_loss = F.kl_div(soft_student, soft_targets, reduction='batchmean') * (temperature ** 2)
    
    return alpha * soft_loss + (1 - alpha) * hard_loss

# Custom trainer
class DistillationTrainer(Trainer):
    def compute_loss(self, model, inputs, return_outputs=False):
        with torch.no_grad():
            teacher_logits = teacher(**inputs).logits
        student_outputs = model(**inputs)
        loss = distillation_loss(student_outputs.logits, teacher_logits, inputs['labels'])
        return (loss, student_outputs) if return_outputs else loss

# Train
trainer = DistillationTrainer(
    model=student,
    args=TrainingArguments(output_dir="./distilled-7b", num_train_epochs=3, learning_rate=2e-5),
    train_dataset=train_dataset,
)
trainer.train()
```

## Decision Tree: Which Technique?

### Choose Pruning When:
- ✅ Have a trained model to compress
- ✅ Want to reduce size without changing architecture
- ✅ Can tolerate slight accuracy loss (<1-3%)
- ✅ Need hardware speedup (with N:M sparsity)
- ✅ Want one-shot compression (no retraining needed)

**Method selection**:
- Wanda: Fast, simple, <1% loss at 50% sparsity
- SparseGPT: Best quality, more compute intensive
- N:M: Hardware acceleration on NVIDIA GPUs (2× speedup)

### Choose Distillation When:
- ✅ Want to compress 70B → 7B (10× reduction)
- ✅ Need to transfer proprietary model knowledge (GPT-4 → open-source)
- ✅ Have compute budget for training
- ✅ Can generate synthetic data from teacher
- ✅ Want to preserve more capability than pruning alone

**Method selection**:
- Standard (forward KLD): Classification, single-answer tasks
- MiniLLM (reverse KLD): Generation, diverse outputs, open-ended tasks

### Combine Both When:
- ✅ Need maximum compression (70B → 7B → pruned 7B)
- ✅ Have both training and inference budget
- ✅ Can afford two-stage pipeline

**Pipeline**:
1. Distill: 70B → 7B (transfer knowledge)
2. Prune: 7B → 50% sparse 7B (reduce size further)
3. Result: 20× total compression

## Core Concepts

### Pruning: Remove Unimportant Weights

```python
# Magnitude pruning (baseline)
importance = |weight|

# Wanda (better)
importance = |weight| × activation

# SparseGPT (best quality)
importance = weight² / Hessian_diagonal
```

**Sparsity types**:
- Unstructured: Prune individual weights (no speedup)
- N:M structured: Keep N of every M weights (hardware speedup)
- Block structured: Prune neurons/heads (coarse, more loss)

### Distillation: Transfer Teacher Knowledge

```python
# Temperature scaling
logits_soft = logits / temperature  # T=2-5 typical

# Loss components
total_loss = alpha * KL(student || teacher) + (1-alpha) * CE(student, labels)
#            ↑ soft (dark knowledge)          ↑ hard (ground truth)
```

**KL divergence types**:
- Forward KL: Mode-seeking (classification)
- Reverse KL: Mode-covering (generation)

## Essential Workflow

### Step 1: Assess Requirements

```python
# What are you optimizing for?
optimization_goals = {
    "size_reduction": True,      # Pruning or distillation
    "speed_increase": True,      # N:M pruning
    "quality_preservation": True,# SparseGPT or careful distillation
    "no_retraining": True,       # One-shot pruning only
}
```

### Step 2: Select Method(s)

```python
if optimization_goals["no_retraining"]:
    method = "wanda"  # or sparsegpt
elif optimization_goals["size_reduction"] > 10:
    method = "distillation"  # Large compression ratio
elif optimization_goals["speed_increase"]:
    method = "nm_pruning"  # Hardware acceleration
else:
    method = "combined"  # Distill then prune
```

### Step 3: Execute

```python
# Pruning
if method in ["wanda", "sparsegpt", "nm_pruning"]:
    compressed_model = prune_model(model, method=method, sparsity=0.5)

# Distillation
elif method == "distillation":
    compressed_model = distill_model(teacher, student, method="minillm")

# Combined
elif method == "combined":
    # Stage 1: Distill
    student = distill_model(teacher, student)
    # Stage 2: Prune
    compressed_model = prune_model(student, sparsity=0.5)
```

### Step 4: Evaluate

```python
from lm_eval import evaluator

results = evaluator.simple_evaluate(
    model="hf",
    model_args=f"pretrained={compressed_model_path}",
    tasks=["arc_easy", "hellaswag", "winogrande"],
)

# Compare vs original
print(f"Accuracy degradation: {original_acc - compressed_acc:.2%}")
print(f"Size reduction: {original_size / compressed_size:.1f}×")
```

## Best Practices

### Sparsity/Compression Ratios

```python
# Conservative (recommended starting point)
sparsity = 0.3       # 30% pruning, <0.5% loss
distill_ratio = 3    # 70B → 24B, ~5% loss

# Balanced (good for production)
sparsity = 0.5       # 50% pruning, ~1% loss
distill_ratio = 10   # 70B → 7B, ~10% loss

# Aggressive (test carefully)
sparsity = 0.7       # 70% pruning, 2-5% loss
distill_ratio = 70   # 70B → 1B, ~20% loss
```

### Avoid Common Pitfalls

```python
# ❌ Bad: Pruning without calibration data
prune_random(model)

# ✅ Good: Use representative calibration data
prune_wanda(model, calib_data)

# ❌ Bad: Distilling with teacher/student size ratio too large
distill(teacher_70B, student_100M)  # 700× gap

# ✅ Good: Reasonable compression ratios
distill(teacher_70B, student_7B)  # 10× gap

# ❌ Bad: Using forward KL for generation tasks
distill(teacher, student, method="forward_kl")

# ✅ Good: Use reverse KL (MiniLLM) for generation
distill(teacher, student, method="reverse_kl")
```

## Performance Comparison

**Compression methods** (LLaMA-7B baseline):

| Method | Size Reduction | Accuracy Loss | Speed | Retraining |
|--------|----------------|---------------|-------|------------|
| Wanda (50%) | 2× | -0.8% | 1.0× | No |
| N:M (2:4) | 2× | -1.0% | 2.0× | No |
| Distill (70B→7B) | 10× | -10% | 1.0× | Yes |
| Combined | 20× | -11% | 2.0× | Yes |

**Source**: Papers cited in frontmatter

## Installation

```bash
# Pruning
git clone https://github.com/locuslab/wanda
cd wanda && pip install -r requirements.txt

# Distillation
pip install transformers datasets accelerate torch

# Optional: MiniLLM
git clone https://github.com/microsoft/LMOps
cd LMOps/minillm && pip install -e .
```

## Resources

**Pruning**:
- Wanda paper: https://arxiv.org/abs/2306.11695
- SparseGPT: https://arxiv.org/abs/2301.00774
- NVIDIA sparse tensors: https://developer.nvidia.com/blog/accelerating-inference-with-sparsity-using-ampere-and-tensorrt/

**Distillation**:
- Hinton et al. 2015: https://arxiv.org/abs/1503.02531
- MiniLLM: https://arxiv.org/abs/2306.08543
- KD Survey: https://arxiv.org/abs/2402.13116
