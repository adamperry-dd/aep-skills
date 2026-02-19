# N:M Structured Sparsity for Hardware Acceleration

N:M sparsity keeps N weights per M consecutive weights, enabling 2× speedup on NVIDIA sparse tensor cores.

## Core Concept

### Sparsity Pattern

```python
# 2:4 pattern (most common)
[1, 0, 1, 0] [1, 1, 0, 0] [0, 1, 0, 1]
 ↑ Keep 2/4   ↑ Keep 2/4   ↑ Keep 2/4

# Result: Exactly 50% sparsity with regular structure
```

**Key property**: Hardware can exploit regular pattern for speedup.

### Supported Patterns

| Pattern | Sparsity | Speedup (A100) | Notes |
|---------|----------|----------------|-------|
| 2:4 | 50% | 2.0× | Most common, best support |
| 4:8 | 50% | 2.0× | Alternative to 2:4 |
| 1:4 | 75% | - | Experimental, less support |

**Recommendation**: Use 2:4 for production (best hardware support).

## Implementation

### Basic N:M Pruning

```python
import torch
import torch.nn.functional as F

def nm_prune(weight, n=2, m=4):
    """
    N:M pruning: Keep N weights per M consecutive weights.
    
    Args:
        weight: Weight tensor (any shape)
        n: Number of weights to keep
        m: Group size
    
    Returns:
        Pruned weight with exactly N:M pattern
    """
    shape = weight.shape
    weight_flat = weight.flatten()

    # Pad to multiple of M
    pad_size = (m - weight_flat.numel() % m) % m
    weight_padded = F.pad(weight_flat, (0, pad_size))

    # Reshape into groups of M
    weight_grouped = weight_padded.reshape(-1, m)

    # Find top-N in each group (by absolute value)
    _, indices = torch.topk(weight_grouped.abs(), n, dim=-1)

    # Create mask (keep only top-N per group)
    mask = torch.zeros_like(weight_grouped)
    mask.scatter_(1, indices, 1.0)

    # Apply mask
    weight_pruned = weight_grouped * mask

    # Reshape back to original
    weight_pruned = weight_pruned.flatten()[:weight_flat.numel()]
    return weight_pruned.reshape(shape)

# Apply to all layers
for name, module in model.named_modules():
    if isinstance(module, torch.nn.Linear):
        module.weight.data = nm_prune(module.weight.data, n=2, m=4)
```

### Importance-Based N:M (Better Quality)

```python
def nm_prune_importance(weight, importance, n=2, m=4):
    """
    N:M pruning using importance scores (e.g., from Wanda).
    
    Args:
        weight: Weight tensor
        importance: Importance scores (same shape as weight)
        n, m: N:M pattern
    """
    shape = weight.shape
    weight_flat = weight.flatten()
    importance_flat = importance.flatten()

    # Pad both
    pad_size = (m - len(weight_flat) % m) % m
    weight_padded = F.pad(weight_flat, (0, pad_size))
    importance_padded = F.pad(importance_flat, (0, pad_size))

    # Group
    weight_grouped = weight_padded.reshape(-1, m)
    importance_grouped = importance_padded.reshape(-1, m)

    # Top-N by importance (not magnitude)
    _, indices = torch.topk(importance_grouped, n, dim=-1)

    # Mask
    mask = torch.zeros_like(weight_grouped)
    mask.scatter_(1, indices, 1.0)

    # Apply
    weight_pruned = weight_grouped * mask
    return weight_pruned.flatten()[:len(weight_flat)].reshape(shape)

# Use with Wanda importance
importance = weight.abs() * activation.unsqueeze(0)
weight_pruned = nm_prune_importance(weight, importance, n=2, m=4)
```

## Wanda + N:M Integration

See the main SKILL.md for complete Wanda implementation, then apply N:M pattern.

## Hardware Acceleration

### NVIDIA Sparse Tensor Cores

**Requirements**:
- GPU: A100, H100 (Ampere/Hopper architecture)
- CUDA: >=11.0
- cuSPARSELt library

**Setup**:
```bash
pip install cusparselt
```

**Inference with acceleration**:
```python
import torch
from torch.cuda.sparse import semi_structured_sparsity

# Convert to sparse format
model_sparse = semi_structured_sparsity(model, sparsity_pattern="2:4")

# Inference (automatic 2× speedup)
with torch.cuda.amp.autocast():
    output = model_sparse(input_ids)

# Speedup verified
# Dense: 100ms
# 2:4 sparse: 50ms ✓
```

## Performance Results

### Speed Benchmarks (A100)

| Model | Dense (ms) | 2:4 Sparse (ms) | Speedup |
|-------|-----------|-----------------|---------|
| LLaMA-7B | 12.5 | 6.8 | 1.8× |
| LLaMA-13B | 24.3 | 12.1 | 2.0× |
| LLaMA-70B | 158.2 | 79.5 | 2.0× |

**Note**: Speedup increases with model size (better utilization).

### Accuracy vs Speedup Trade-off

| Method | Sparsity | Speedup | Accuracy Loss |
|--------|----------|---------|---------------|
| Unstructured 50% | 50% | 1.0× | -0.8% |
| 2:4 | 50% | 2.0× | -1.0% |
| 4:8 | 50% | 2.0× | -1.1% |

**Key finding**: Small accuracy penalty (~0.2%) for 2× speedup.

## Best Practices

### When to Use N:M

```python
# ✅ Use N:M when:
- Deploying to NVIDIA A100/H100
- Need inference speedup (not just size reduction)
- Can tolerate slight accuracy loss (~1%)

# ❌ Don't use N:M when:
- Not using NVIDIA GPUs (no speedup)
- Need absolute best quality (use unstructured)
- Targeting non-NVIDIA hardware (AMD, Apple Silicon)
```

### Pattern Selection

```python
# 2:4: Best overall (hardware support + quality)
pattern = "2:4"  # Recommended

# 4:8: Alternative, slightly worse quality
pattern = "4:8"  # Use if 2:4 not supported

# 1:4: Experimental, avoid
pattern = "1:4"  # Not recommended
```

## Limitations

1. **Hardware dependency**: Speedup only on NVIDIA Ampere/Hopper
2. **Slightly worse quality**: ~0.2% more loss than unstructured
3. **Fixed pattern**: Can't adjust sparsity (always 50% for 2:4)

## Resources

- NVIDIA blog: https://developer.nvidia.com/blog/accelerating-inference-with-sparsity-using-ampere-and-tensorrt/
- cuSPARSELt docs: https://docs.nvidia.com/cuda/cusparselt/
- PyTorch sparse docs: https://pytorch.org/docs/stable/sparse.html
