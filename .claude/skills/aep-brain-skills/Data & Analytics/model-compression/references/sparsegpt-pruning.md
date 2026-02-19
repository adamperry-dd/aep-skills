# SparseGPT: Second-Order Pruning

Based on arXiv 2301.00774 - SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot

**GitHub**: https://github.com/IST-DASLab/sparsegpt

## Core Innovation

### Second-Order Importance

**Key insight**: Use Hessian (second derivative) for more accurate importance scoring.

```python
importance = weight² / diag(Hessian)

where Hessian captures loss curvature (sensitivity)
```

**Why better than magnitude**:
- Magnitude: Only considers weight size
- Wanda: Considers weight × activation
- **SparseGPT**: Considers loss sensitivity (most accurate)

## Algorithm

### Layer-wise Reconstruction

```python
def sparsegpt_prune(model, calib_data, sparsity=0.5):
    """
    SparseGPT pruning with layer-wise reconstruction.
    
    Steps per layer:
    1. Compute Hessian inverse on calibration data
    2. Prune weights with lowest importance
    3. Reconstruct remaining weights to minimize error
    """
    for layer in model.layers:
        # 1. Collect Hessian (second derivative of loss)
        H = compute_hessian(layer, calib_data)
        
        # 2. Compute importance scores
        W = layer.weight.data
        importance = W ** 2 / torch.diag(H)
        
        # 3. Prune lowest importance weights
        threshold = torch.quantile(importance.flatten(), sparsity)
        mask = importance >= threshold
        
        # 4. Reconstruct remaining weights (minimize error)
        W_pruned = reconstruct_weights(W, mask, H)
        layer.weight.data = W_pruned
    
    return model

def reconstruct_weights(W, mask, H):
    """
    Optimal weight reconstruction after pruning.
    
    Solves: W_new = argmin ||W_new - W||²_H subject to mask
    """
    # Damped Hessian inverse (for numerical stability)
    H_inv = torch.inverse(H + 0.01 * torch.eye(H.size(0)))
    
    # Reconstruct pruned weights
    W_new = W.clone()
    W_new[~mask] = 0
    
    # Adjust remaining weights to compensate
    for i in range(W.size(0)):
        if mask[i]:
            delta = -torch.sum(W[~mask] * H_inv[i, ~mask]) / H_inv[i, i]
            W_new[i] += delta
    
    return W_new
```

## Installation

```bash
git clone https://github.com/IST-DASLab/sparsegpt
cd sparsegpt
pip install -e .
```

## Usage

### Basic Pruning

```python
from sparsegpt import SparseGPT

# Load model
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")

# Initialize pruner
pruner = SparseGPT(model)

# Calibration data (128 samples recommended)
calib_data = load_calibration_data()

# Prune (one-shot, layer-wise reconstruction)
pruned_model = pruner.prune(
    calib_data=calib_data,
    sparsity=0.5,           # 50% sparsity
    prunen=0,               # Unstructured (0) or N:M structured
    prunem=0,
    percdamp=0.01,          # Damping for Hessian inverse (numerical stability)
)

# Save
pruned_model.save_pretrained("./llama-7b-sparsegpt-50")
```

### Structured (N:M) Pruning

```python
# 2:4 sparsity for NVIDIA GPUs
pruned_model = pruner.prune(
    calib_data=calib_data,
    sparsity=0.5,
    prunen=2,    # Keep 2 out of every 4
    prunem=4,
)
```

## Performance Results

**From paper** (LLaMA models):

| Model | Sparsity | Method | WikiText2 PPL | C4 PPL |
|-------|----------|--------|---------------|---------|
| LLaMA-7B | 0% | Baseline | 5.68 | 7.08 |
| LLaMA-7B | 50% | Magnitude | 8.45 | 10.12 |
| LLaMA-7B | 50% | **SparseGPT** | **6.32** | **7.89** |

**Key finding**: Near-lossless pruning at 50% sparsity (<0.5% degradation).

### High Sparsity Results

| Sparsity | WikiText2 PPL | Degradation |
|----------|---------------|-------------|
| 0% | 5.68 | Baseline |
| 50% | 6.32 | +0.64 |
| 60% | 7.21 | +1.53 |
| 70% | 10.15 | +4.47 |

**Recommendation**: Stay below 60% for minimal degradation.

## Hyperparameters

### Damping Factor (percdamp)

```python
percdamp = 0.01   # Standard (from paper)
percdamp = 0.001  # Less damping (more aggressive reconstruction)
percdamp = 0.1    # More damping (more conservative, numerically stable)
```

**Rule**: Use 0.01 as default, increase if seeing numerical instability.

### Calibration Data Size

```python
# Minimum
calib_samples = 64   # Works but slightly lower quality

# Standard (from paper)
calib_samples = 128  # Good balance

# Maximum benefit
calib_samples = 256  # Marginal improvement beyond 128
```

## Computational Cost

**Memory**: O(d²) per layer (Hessian matrix)
- LLaMA-7B: ~4GB extra VRAM
- LLaMA-70B: ~40GB extra VRAM (use DeepSpeed)

**Time**: ~1-2 hours for 7B model on A100

### Optimization for Large Models

```python
# Use DeepSpeed for memory efficiency
from deepspeed import zero

pruner = SparseGPT(model, device_map="auto")
pruned_model = pruner.prune(
    calib_data=calib_data,
    sparsity=0.5,
    use_zero=True,  # Enable ZeRO optimization
)
```

## Comparison: SparseGPT vs Wanda

**When to use SparseGPT**:
- Need best possible quality (<0.5% loss at 50%)
- Have compute budget (hours)
- Have memory for Hessian computation

**When to use Wanda**:
- Need fast pruning (minutes)
- Limited memory
- Accept slightly lower quality (~0.8% loss at 50%)

**Trade-off table**:

| Metric | SparseGPT | Wanda |
|--------|-----------|-------|
| Quality | ★★★★★ | ★★★★☆ |
| Speed | ★★☆☆☆ | ★★★★★ |
| Memory | ★★☆☆☆ | ★★★★★ |
| Simplicity | ★★☆☆☆ | ★★★★★ |

## Limitations

1. **Computational cost**: Requires Hessian computation (memory intensive)
2. **No speedup**: Unstructured sparsity (unless using N:M variant)
3. **One-shot only**: Can't iteratively adjust

## Resources

- Paper: https://arxiv.org/abs/2301.00774
- GitHub: https://github.com/IST-DASLab/sparsegpt
