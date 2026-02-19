# Evaluation & Benchmarks for Compressed Models

Comprehensive evaluation strategies and benchmark results.

## Evaluation Frameworks

### LM Evaluation Harness

**Most common tool**: https://github.com/EleutherAI/lm-evaluation-harness

```bash
# Install
pip install lm-eval

# Evaluate model
lm_eval --model hf \
    --model_args pretrained=./compressed-model \
    --tasks arc_easy,arc_challenge,hellaswag,winogrande,truthfulqa \
    --batch_size 8 \
    --output_path ./results.json
```

**Standard benchmark suite**:
- ARC (easy + challenge): Reasoning
- HellaSwag: Common sense
- WinoGrande: Coreference resolution
- TruthfulQA: Truthfulness
- MMLU: Multi-task understanding

### Custom Evaluation Script

```python
from lm_eval import evaluator
from transformers import AutoModelForCausalLM

def evaluate_compression(original_path, compressed_path):
    """
    Compare original vs compressed model.
    """
    tasks = ["arc_easy", "arc_challenge", "hellaswag", "winogrande"]
    
    # Evaluate original
    original_results = evaluator.simple_evaluate(
        model="hf",
        model_args=f"pretrained={original_path}",
        tasks=tasks,
    )
    
    # Evaluate compressed
    compressed_results = evaluator.simple_evaluate(
        model="hf",
        model_args=f"pretrained={compressed_path}",
        tasks=tasks,
    )
    
    # Compare
    print("=== Comparison ===")
    for task in tasks:
        orig_acc = original_results['results'][task]['acc']
        comp_acc = compressed_results['results'][task]['acc']
        degradation = orig_acc - comp_acc
        retention = comp_acc / orig_acc
        
        print(f"{task}:")
        print(f"  Original:    {orig_acc:.3f}")
        print(f"  Compressed:  {comp_acc:.3f}")
        print(f"  Degradation: {degradation:.3f}")
        print(f"  Retention:   {retention:.1%}")
```

## Benchmark Results

### Pruning Methods (50% Sparsity)

**LLaMA-7B baseline**: 60.2% average accuracy

| Method | Avg Accuracy | Degradation | Speedup |
|--------|--------------|-------------|---------|
| Baseline (dense) | 60.2% | - | 1.0× |
| Magnitude pruning | 55.3% | -4.9% | 1.0× |
| **Wanda** | **59.4%** | **-0.8%** | 1.0× |
| SparseGPT | 59.8% | -0.4% | 1.0× |
| N:M (2:4) | 59.2% | -1.0% | 2.0× |

**Source**: Wanda ICLR 2024, SparseGPT papers

### Distillation Methods

**Teacher: LLaMA-70B (70.1% avg accuracy)**

| Student | Method | Avg Accuracy | Retention | Size Reduction |
|---------|--------|--------------|-----------|----------------|
| LLaMA-13B | Baseline | 62.3% | - | 5.4× |
| LLaMA-13B | Standard KD | 65.1% | 92.9% | 5.4× |
| LLaMA-7B | Baseline | 60.2% | - | 10× |
| LLaMA-7B | Standard KD | 62.8% | 89.6% | 10× |
| LLaMA-7B | **MiniLLM (Reverse KLD)** | **64.1%** | **91.4%** | 10× |

**Source**: MiniLLM paper, KD surveys

### Combined Compression

**Pipeline: 70B → 7B (distill) → 50% sparse (prune)**

| Stage | Size | Accuracy | Speedup |
|-------|------|----------|---------|
| LLaMA-70B (baseline) | 70B | 70.1% | 1.0× |
| After distillation | 7B | 64.1% | 10× smaller |
| After pruning | 3.5B equiv | 62.9% | 10× smaller, 2× faster |

**Total compression**: 20× smaller, 2× faster, -7.2% accuracy

## Perplexity Benchmarks

### WikiText-2

| Model | Sparsity/Method | Perplexity | Degradation |
|-------|-----------------|------------|-------------|
| LLaMA-7B | Dense | 5.68 | Baseline |
| LLaMA-7B | Wanda 50% | 6.18 | +0.50 |
| LLaMA-7B | SparseGPT 50% | 6.32 | +0.64 |
| LLaMA-7B | Magnitude 50% | 8.45 | +2.77 |

**Lower is better**. <1.0 degradation is excellent.

## Generative Quality Metrics

### MT-Bench (Conversational)

**Scale**: 1-10 (higher is better)

| Model | Method | MT-Bench Score |
|-------|--------|----------------|
| LLaMA-70B | Baseline | 6.9 |
| LLaMA-7B | Baseline | 5.2 |
| LLaMA-7B | Standard distill | 5.8 |
| LLaMA-7B | MiniLLM | 6.4 |

### AlpacaEval (Instruction Following)

**Win rate vs GPT-4**:

| Model | Method | Win Rate |
|-------|--------|----------|
| LLaMA-70B | Baseline | 78% |
| LLaMA-7B | Baseline | 55% |
| LLaMA-7B | MiniLLM | 71% |

## Inference Speed Benchmarks

### Latency (ms per token)

**Hardware**: NVIDIA A100

| Model | Dense | Wanda 50% | N:M 2:4 |
|-------|-------|-----------|---------|
| LLaMA-7B | 12.5 | 12.5 | 6.8 |
| LLaMA-13B | 24.3 | 24.3 | 12.1 |
| LLaMA-70B | 158.2 | 158.2 | 79.5 |

**Key finding**: N:M achieves ~2× speedup on NVIDIA hardware.

## Quality vs Efficiency Trade-offs

### Compression Decision Matrix

| Accuracy Tolerance | Size Reduction | Recommended Method |
|-------------------|----------------|-------------------|
| <1% loss | 2× | Wanda/SparseGPT 50% |
| ~5% loss | 5× | Distill 70B→13B |
| ~10% loss | 10× | Distill 70B→7B |
| ~15% loss | 20× | Distill + Prune |
| >20% loss | 50×+ | Aggressive pipeline |

## Evaluation Best Practices

### Comprehensive Evaluation Checklist

```python
evaluation_suite = {
    # Accuracy
    "zero_shot": ["arc_easy", "hellaswag", "winogrande"],
    "reasoning": ["arc_challenge", "piqa"],
    "knowledge": ["mmlu"],
    "truthfulness": ["truthfulqa"],
    
    # Generation quality
    "conversational": ["mt_bench"],
    "instruction": ["alpaca_eval"],
    
    # Perplexity
    "language_modeling": ["wikitext2", "c4"],
    
    # Speed
    "latency": "measure_tokens_per_second",
    "throughput": "measure_batch_throughput",
    
    # Memory
    "model_size": "check_disk_size",
    "inference_memory": "measure_vram_usage",
}
```

## Resources

- LM Eval Harness: https://github.com/EleutherAI/lm-evaluation-harness
- MT-Bench: https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge
- AlpacaEval: https://github.com/tatsu-lab/alpaca_eval
- Open LLM Leaderboard: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
