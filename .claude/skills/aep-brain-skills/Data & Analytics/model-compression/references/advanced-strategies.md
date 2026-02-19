# Advanced Compression Strategies

Combining techniques and advanced patterns for maximum compression.

## Combined Pruning + Distillation

### Sequential Pipeline

**Best approach**: Distill first, then prune.

```python
def compress_pipeline(
    large_teacher,
    medium_student,
    target_sparsity=0.5
):
    """
    Two-stage compression:
    1. Distill: 70B → 7B (10× compression)
    2. Prune: 7B → 50% sparse (2× compression)
    Result: 20× total compression
    """
    # Stage 1: Distillation
    print("Stage 1: Distilling 70B → 7B...")
    distilled_model = distill_model(
        teacher=large_teacher,
        student=medium_student,
        method="minillm",  # Use reverse KLD for generation
        epochs=5
    )
    
    # Stage 2: Pruning
    print("Stage 2: Pruning 7B → 50% sparse...")
    compressed_model = prune_model(
        model=distilled_model,
        method="wanda",
        sparsity=target_sparsity
    )
    
    return compressed_model

# Usage
final_model = compress_pipeline(
    large_teacher=llama_70b,
    medium_student=llama_7b,
    target_sparsity=0.5
)

# Result:
# Size: 70B → 3.5B equivalent (20× reduction)
# Quality: ~12-15% accuracy loss (vs 70B baseline)
# Speed: 2× faster inference (with N:M sparsity)
```

**Why distill first**:
- Distillation needs dense weights for knowledge transfer
- Pruning sparse model is easier than distilling sparse model
- Better final accuracy

## Gradual Pruning

Incrementally increase sparsity during training.

```python
def gradual_prune(
    model,
    initial_sparsity=0.0,
    final_sparsity=0.5,
    num_steps=100
):
    """
    Gradually increase sparsity over training.
    Better than one-shot at high sparsity (>60%).
    """
    optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)
    
    for step in range(num_steps):
        # Current sparsity (linear schedule)
        current_sparsity = initial_sparsity + \
            (final_sparsity - initial_sparsity) * (step / num_steps)
        
        # Prune at current sparsity
        for module in model.modules():
            if isinstance(module, torch.nn.Linear):
                weight = module.weight.data
                threshold = torch.quantile(weight.abs().flatten(), current_sparsity)
                mask = weight.abs() >= threshold
                weight *= mask.float()
        
        # Train one step
        train_step(model, optimizer)
    
    return model

# Best for high sparsity (70-90%)
model = gradual_prune(model, final_sparsity=0.7, num_steps=1000)
```

## Layer-wise Pruning

Different sparsity for different layers.

```python
def layer_wise_prune(model, sparsity_schedule):
    """
    Apply different sparsity to different layers.
    
    Strategy: Early layers less pruning (more important)
              Late layers more pruning (less critical)
    """
    # Sparsity schedule
    schedule = {
        "layer.0": 0.3,   # 30% sparsity (important early layers)
        "layer.1": 0.4,
        "layer.2": 0.5,
        "layer.3": 0.6,   # 60% sparsity (less critical late layers)
    }
    
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Linear):
            # Find matching layer
            for layer_pattern, sparsity in schedule.items():
                if layer_pattern in name:
                    # Prune at layer-specific sparsity
                    weight = module.weight.data
                    threshold = torch.quantile(weight.abs().flatten(), sparsity)
                    mask = weight.abs() >= threshold
                    weight *= mask.float()
                    break
    
    return model
```

## Multi-Teacher Distillation

Learn from ensemble of expert teachers.

```python
def multi_teacher_distillation(student, teachers, batch):
    """
    Distill from multiple teachers simultaneously.
    
    Use cases:
    - Ensemble of domain experts
    - Different model architectures
    - Diverse teacher capabilities
    """
    teacher_logits_list = []
    
    # Get logits from all teachers
    with torch.no_grad():
        for teacher in teachers:
            logits = teacher(**batch).logits
            teacher_logits_list.append(logits)
    
    # Average teacher predictions (or weighted average)
    avg_teacher_logits = torch.stack(teacher_logits_list).mean(dim=0)
    
    # Student learns from ensemble
    student_logits = student(**batch).logits
    loss = F.kl_div(
        F.log_softmax(student_logits, dim=-1),
        F.softmax(avg_teacher_logits, dim=-1),
        reduction='batchmean'
    )
    
    return loss

# Usage
teachers = [llama_70b, mistral_7b, gpt_j_6b]  # Diverse experts
student = distill_from_ensemble(student, teachers)
```

## Best Practices Summary

### When to Use Each Strategy

```python
# One-shot pruning (Wanda/SparseGPT)
if sparsity <= 0.6 and no_training_budget:
    use_strategy = "one_shot"

# Gradual pruning
if sparsity > 0.6 and have_training_budget:
    use_strategy = "gradual"

# Distill + Prune
if size_reduction > 10:
    use_strategy = "distill_then_prune"

# Multi-teacher
if have_multiple_experts:
    use_strategy = "multi_teacher"
```

### Compression Budget vs Quality

| Target | Strategy | Accuracy Loss | Time |
|--------|----------|---------------|------|
| 2× | One-shot Wanda 50% | <1% | Minutes |
| 5× | Distill 70B→13B | ~5% | Hours |
| 10× | Distill 70B→7B | ~10% | Hours |
| 20× | Distill + Prune | ~15% | Days |
| 50× | Aggressive pipeline | ~25% | Days |

## Resources

- Gradual pruning: https://arxiv.org/abs/1710.01878
- Multi-teacher: https://arxiv.org/abs/1711.02613
- Layer distillation: https://arxiv.org/abs/1503.02531
