# Standard Knowledge Distillation for LLMs

Based on Hinton et al. 2015 (arXiv 1503.02531) - Distilling the Knowledge in a Neural Network

## Core Principles

### Teacher-Student Framework

**Setup**:
- **Teacher**: Large, high-performance model (e.g., LLaMA-70B)
- **Student**: Small, efficient model (e.g., LLaMA-7B)
- **Goal**: Transfer teacher's knowledge to student

**Key insight**: Teacher's full probability distribution contains more information than hard labels alone.

## Temperature Scaling

### Softening Distributions

```python
def temperature_softmax(logits, temperature):
    """Soften probability distribution to expose teacher's uncertainty."""
    return F.softmax(logits / temperature, dim=-1)

# Example
logits = [3.0, 2.0, 1.0]

# Low temperature (T=1): Sharp
probs_T1 = softmax(logits / 1.0)  # [0.67, 0.24, 0.09]

# High temperature (T=4): Soft
probs_T4 = softmax(logits / 4.0)  # [0.42, 0.34, 0.24]
```

**Why soft targets help**:
- Reveals relative rankings (2nd best, 3rd best, etc.)
- Exposes teacher's uncertainty
- Provides richer training signal

**Typical values**: T = 2-5 (T=2 is common default)

## Distillation Loss

### Combined Loss Function

```python
def distillation_loss(
    student_logits,
    teacher_logits,
    labels,
    temperature=2.0,
    alpha=0.7
):
    """
    Combine soft loss (from teacher) with hard loss (from labels).
    
    Args:
        temperature: Softening parameter (2-5 typical)
        alpha: Weight for soft loss (0-1)
               alpha=1.0 → only teacher knowledge
               alpha=0.0 → only ground truth labels
    """
    # Soft loss: KL divergence between distributions
    soft_targets = F.softmax(teacher_logits / temperature, dim=-1)
    soft_student = F.log_softmax(student_logits / temperature, dim=-1)
    soft_loss = F.kl_div(
        soft_student,
        soft_targets,
        reduction='batchmean'
    ) * (temperature ** 2)  # Temperature correction
    
    # Hard loss: Cross-entropy with true labels
    hard_loss = F.cross_entropy(
        student_logits.view(-1, student_logits.size(-1)),
        labels.view(-1)
    )
    
    # Weighted combination
    return alpha * soft_loss + (1 - alpha) * hard_loss
```

## Implementation

### Basic Distillation Training

```python
import torch
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

# Custom trainer with distillation
class DistillationTrainer(Trainer):
    def __init__(self, *args, teacher_model=None, temperature=2.0, alpha=0.7, **kwargs):
        super().__init__(*args, **kwargs)
        self.teacher = teacher_model
        self.temperature = temperature
        self.alpha = alpha
    
    def compute_loss(self, model, inputs, return_outputs=False):
        # Student forward
        outputs_student = model(**inputs)
        student_logits = outputs_student.logits
        
        # Teacher forward (no gradient)
        with torch.no_grad():
            outputs_teacher = self.teacher(**inputs)
            teacher_logits = outputs_teacher.logits
        
        # Distillation loss
        loss = distillation_loss(
            student_logits,
            teacher_logits,
            inputs['labels'],
            temperature=self.temperature,
            alpha=self.alpha
        )
        
        return (loss, outputs_student) if return_outputs else loss

# Train
trainer = DistillationTrainer(
    model=student,
    args=TrainingArguments(output_dir="./distilled-llama-7b", num_train_epochs=3, learning_rate=2e-5),
    train_dataset=train_dataset,
    teacher_model=teacher,
    temperature=2.0,
    alpha=0.7,
)

trainer.train()
student.save_pretrained("./distilled-llama-7b")
```

## Hyperparameter Selection

### Temperature

```python
# Low temperature (sharp distributions)
T = 1.0  # Minimal softening, less knowledge transfer

# Medium temperature (balanced)
T = 2.0  # Standard choice (recommended)
T = 3.0  # More softening

# High temperature (very soft)
T = 5.0  # Maximum knowledge transfer, risk of noise
```

**Rule of thumb**:
- Start with T=2.0
- Increase if student underfitting
- Decrease if student overfitting to soft targets

### Alpha (Loss Weight)

```python
# Balanced
alpha = 0.5  # Equal weight to teacher and labels

# Teacher-focused
alpha = 0.7  # More emphasis on teacher (common)
alpha = 0.9  # Strong distillation

# Label-focused
alpha = 0.3  # More emphasis on ground truth
```

**Guidelines**:
- High alpha (0.7-0.9): When teacher is very reliable
- Low alpha (0.3-0.5): When labels are important
- Medium alpha (0.5): When uncertain

## Best Practices

### Model Size Ratios

```python
# Good ratios (teacher/student)
70B / 7B = 10×    # Excellent
13B / 1.3B = 10×  # Good
7B / 700M = 10×   # Acceptable

# Avoid extreme gaps
70B / 1B = 70×    # Too large, ineffective
7B / 7B = 1×      # No compression
```

**Rule**: 5-15× compression ratio works best.

## Resources

- Foundational paper: https://arxiv.org/abs/1503.02531
- Survey on KD for LLMs: https://arxiv.org/abs/2402.13116
- HuggingFace guide: https://huggingface.co/docs/transformers/main/en/tasks/knowledge_distillation
