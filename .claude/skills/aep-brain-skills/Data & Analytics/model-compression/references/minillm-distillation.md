# MiniLLM: Reverse KL Divergence for LLM Distillation

Based on arXiv 2306.08543 (2024) - MiniLLM: Knowledge Distillation of Large Language Models

**GitHub**: https://github.com/microsoft/LMOps/tree/main/minillm

## Problem with Standard KLD

### Forward KL (Standard Distillation)

**Formula**: `KL(Student || Teacher)`

**Behavior**: Mode-seeking
```
Student matches teacher's MEAN behavior
→ Focuses on highest probability regions
→ Ignores low-probability but valid generations
```

**Example**:
```python
# Teacher distribution (diverse)
teacher_probs = [0.3, 0.3, 0.2, 0.1, 0.1]  # Multiple valid options

# Forward KL student learns:
student_probs = [0.6, 0.3, 0.1, 0.0, 0.0]  # Mode-seeking
# Problem: Ignores options 4-5 (less diverse generation)
```

**Issue**: Poor for generative models (limited diversity, boring outputs).

## MiniLLM Solution: Reverse KLD

### Reverse KL Divergence

**Formula**: `KL(Teacher || Student)`

**Behavior**: Mode-covering
```
Student covers ALL teacher's modes
→ Learns diverse generation
→ Doesn't ignore any valid teacher outputs
```

**Mathematical difference**:

```python
# Forward KL (standard)
L_forward = E[x~student] [log p_student(x) - log p_teacher(x)]

# Reverse KL (MiniLLM)
L_reverse = E[x~teacher] [log p_teacher(x) - log p_student(x)]
```

**Key**: Expectation over **teacher** distribution, not student.

## Implementation

### Reverse KLD Loss

```python
import torch
import torch.nn.functional as F

def reverse_kl_loss(student_logits, teacher_logits, temperature=1.0):
    """
    Reverse KL divergence: KL(Teacher || Student).
    
    Args:
        student_logits: (batch, seq_len, vocab_size)
        teacher_logits: (batch, seq_len, vocab_size)
        temperature: Softening parameter
    """
    # Teacher distribution (target, detached)
    p_teacher = F.softmax(teacher_logits / temperature, dim=-1).detach()
    
    # Student distribution (learnable)
    log_p_student = F.log_softmax(student_logits / temperature, dim=-1)
    
    # Reverse KL: -Σ p_teacher * log p_student
    reverse_kl = -(p_teacher * log_p_student).sum(dim=-1).mean()
    
    # Temperature correction
    return reverse_kl * (temperature ** 2)
```

## Training Procedure

### Complete Training Script

```python
from transformers import AutoModelForCausalLM, Trainer, TrainingArguments

def train_minillm(
    teacher_name="meta-llama/Llama-2-70b-hf",
    student_name="meta-llama/Llama-2-7b-hf",
    output_dir="./minillm-7b",
):
    # Load models
    teacher = AutoModelForCausalLM.from_pretrained(
        teacher_name,
        torch_dtype=torch.float16,
        device_map="auto"
    )
    student = AutoModelForCausalLM.from_pretrained(
        student_name,
        torch_dtype=torch.float16
    )

    # Custom trainer
    class MiniLLMTrainer(Trainer):
        def compute_loss(self, model, inputs, return_outputs=False):
            # Generate from teacher
            with torch.no_grad():
                teacher_outputs = teacher.generate(
                    inputs['input_ids'],
                    max_new_tokens=256,
                    do_sample=True,
                    return_dict_in_generate=True,
                    output_scores=True
                )
                teacher_sequences = teacher_outputs.sequences
                teacher_logits = torch.stack(teacher_outputs.scores, dim=1)

            # Student evaluates
            student_outputs = model(
                input_ids=teacher_sequences,
                labels=teacher_sequences
            )

            # Reverse KL
            loss = reverse_kl_loss(student_outputs.logits, teacher_logits)

            return (loss, student_outputs) if return_outputs else loss

    # Train
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=5,
        per_device_train_batch_size=2,
        gradient_accumulation_steps=16,
        learning_rate=5e-5,  # Higher than standard distillation
        warmup_steps=1000,
        bf16=True,
    )

    trainer = MiniLLMTrainer(
        model=student,
        args=training_args,
        train_dataset=train_dataset,
    )

    trainer.train()
    student.save_pretrained(output_dir)
```

## Performance Results

**From paper** (LLaMA models):

| Student | Teacher | Method | MT-Bench | AlpacaEval |
|---------|---------|--------|----------|------------|
| LLaMA-7B | - | Baseline | 5.2 | 55% |
| LLaMA-7B | LLaMA-70B | Forward KL | 5.8 | 62% |
| LLaMA-7B | LLaMA-70B | **Reverse KL** | **6.4** | **71%** |

**Key finding**: Reverse KL outperforms forward KL by ~10% on generation tasks.

## When to Use Forward vs Reverse KL

### Forward KL (Standard)

**Use when**:
- Classification tasks
- Single correct answer
- Deterministic output needed
- Less diverse generation acceptable

**Example tasks**: Sentiment analysis, Q&A with single answer

### Reverse KL (MiniLLM)

**Use when**:
- Generative tasks
- Multiple valid outputs
- Diversity important
- Open-ended generation

**Example tasks**: Creative writing, dialogue, summarization

## Hyperparameters

### Temperature

```python
T = 1.0  # Standard (from paper, recommended)
T = 0.8  # Sharper (less diversity)
T = 1.2  # Softer (more diversity)
```

**Rule**: Use T=1.0 for MiniLLM (higher temps help mode-covering).

### Learning Rate

```python
lr_forward_kl = 2e-5   # Standard distillation
lr_minillm = 5e-5      # MiniLLM (can handle higher LR)
```

**Reason**: Reverse KL has better gradient properties.

## Limitations

1. **Computational cost**: Requires sampling from teacher during training
2. **Memory**: Need to store teacher-generated samples
3. **Complexity**: More complex than standard distillation

## Resources

- Paper: https://arxiv.org/abs/2306.08543
- GitHub: https://github.com/microsoft/LMOps/tree/main/minillm
- Blog: https://www.microsoft.com/en-us/research/blog/minillm-small-language-models-via-large-language-model-distillation/
