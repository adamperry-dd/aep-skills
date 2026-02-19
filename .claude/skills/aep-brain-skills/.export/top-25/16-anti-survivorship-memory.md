---
name: anti-survivorship-memory
description: "Universal skill to reduce survivorship/selection bias and mitigate short-term memory limits in AI assistants and agents. Designed for Constitutional-AI-style setups + vector (RAG) memory. Use when: (1) making recommendations or causal claims from examples, (2) analyzing performance/metrics where failures are underreported, (3) summarizing success stories, playbooks, or best practices, (4) building agentic systems with long-running tasks, (5) any workflow using vector retrieval for memory or knowledge."
---

# Anti-Survivorship & Durable Memory Skill

This skill prevents two predictable failure modes:

1) **Survivorship bias / selection bias**  
   Drawing conclusions from the visible “survivors” (success cases, retained users, shipped projects, published papers), while missing the non-survivors (failures, churned users, abandoned drafts, rejected experiments). The classic Wald aircraft analysis is the canonical illustration: you must reason about what *didn’t* return, not just what did.

2) **Short-term memory failure**  
   Confusing “I once saw it earlier in the conversation” with “I will reliably use it later.” LLMs have finite working context; long-context performance can be brittle (often worst for information buried in the middle). A durable assistant needs an external memory layer and an explicit *context re-anchoring* routine.

**Design goals**
- **Universal**: model-agnostic, framework-agnostic.
- **Constitutional**: principle set + self-critique loop.
- **Vector memory**: retrieval-augmented, persistent, with metadata.
- **Bias-resistant**: retrieval and write-back policies explicitly include failures and counterexamples.

---

## File Intake Workflow

When triggered, request only what you need to reduce guesswork and selection bias.

| Task | Required Inputs | Nice-to-Have Inputs |
|------|-----------------|---------------------|
| Recommendation / decision | goal, constraints, alternatives considered, audience, success criteria | base rates, failure rates, historical attempts, risk tolerance |
| Metrics / analytics | denominator definition, full population window, inclusion/exclusion rules | dropout/churn logs, missing-data report, cohort definitions |
| RAG / memory QA | allowed sources, citation/provenance requirement, memory retention policy | retrieval eval set, “must not forget” list |
| Long-running assistant | project goal, standing constraints, decision log format | owner preferences, risk/ethical constraints, privacy rules |

### Intake validation (must do)
Before answering, explicitly identify:
1. **Target population** (what we want to generalize about)
2. **Observed sample** (what we can actually see)
3. **Selection mechanism** (why cases are missing)
4. **Denominators / base rates** (counts, not vibes)
5. **Missingness type** (random vs systematic vs unknown)

If any are unknown, label survivorship risk **HIGH** and keep conclusions conditional.

---

## Definitions

### Survivorship bias (operational definition)
A reasoning error where the assistant treats *observed successes* as representative of the population, without accounting for unobserved failures filtered out by the selection process.

### Selection mechanism (what filtered reality)
Examples:
- “Only companies that survived long enough to be famous”
- “Only users who kept using the product long enough to leave feedback”
- “Only experiments that got published”
- “Only projects that made it to launch”

### Durable memory (what ‘remember’ should mean here)
The assistant can reliably:
- preserve hard constraints,
- recall prior decisions and rationales,
- retrieve relevant counterexamples and failures,
- cite where a remembered fact came from (provenance),
even when the conversation is long or multi-session.

---

## Memory Architecture (Vector + Constitutional)

### Memory tiers (universal pattern)
1. **Working context (short-term)**: current prompt/context window.
2. **Episodic vector memory (long-term, event-like)**: past interactions, decisions, outcomes.
3. **Semantic memory (stable rules/policies)**: the “constitution,” definitions, SOPs.
4. **Audit trail (immutable log)**: what was retrieved, used, ignored, and why.

### Memory schema (required metadata)
Every stored memory chunk MUST include:

- `id`: unique
- `timestamp`: ISO-8601
- `type`: `fact | preference | constraint | decision | failure | near_miss | counterexample | unknown`
- `outcome`: `success | failure | mixed | unknown`
- `source`: `user | doc | system | tool | web`
- `confidence`: `high | medium | low`
- `scope`: `session | project | global`
- `text`: the content
- `provenance`: link, citation, doc pointer, or “user-stated on YYYY-MM-DD”

**Structural anti-bias rule**: if you don’t tag failures/counterexamples explicitly, your memory will *bake in* survivorship bias because retrieval will over-surface happy-path content.

---

## Core Workflows

### 1) Survivorship Bias Pre-Check (always run first)

Use before giving:
- advice, recommendations, strategies
- causal explanations (“X causes Y”)
- best-practice summaries
- performance conclusions (especially from “success stories”)

**Checklist**
```
1. Restate the user request as a testable claim.
2. Identify:
   a) target population
   b) observed sample
   c) selection mechanism
3. Ask: “Who/what is missing, and why?”
4. Ask: “If missing cases were included, how could this conclusion change?”
5. If denominators or failure data are missing:
   - mark survivorship risk HIGH
   - provide bounds (best-case/worst-case)
   - avoid strong causal claims
```

---

### 2) Retrieval Plan (Vector) — Balanced + Contrastive

**Goal**: retrieve relevance *and* counterevidence.

**Balanced retrieval recipe**
```
A) top_k similar (general relevance)
B) top_k where type in {failure, near_miss, counterexample}
C) top_k where outcome = failure
D) diversity set: enforce source diversity (user/docs/tools/web)
E) (optional) rerank with a cross-encoder or LLM reranker
F) log: query, filters, scores, selected set
```

**Quota rule**
- If the final retrieved set is >70% “success” outcome, increase (B) and (C) until you have meaningful failure/counterexample coverage.

---

### 3) “Wald Audit” for any dataset/story (bullet-hole test)

Apply this whenever evidence is mainly “what we can see.”

```
1. List observed signals (visible evidence).
2. List unobserved signals (what would prevent visibility/survival).
3. Ask: “Which missing signals would reverse my recommendation?”
4. Seek data about non-survivors (failures, churn, rejections).
5. If unavailable:
   - state limitation clearly
   - switch from point-estimate to scenario bounds
   - recommend low-regret experiments over irreversible commitments
```

---

### 4) Short-Term Memory Guardrail (context re-anchoring)

Run when:
- conversation is long,
- the user has many constraints,
- or the assistant is making multi-step plans.

**Procedure**
```
1. Extract hard constraints (must-haves / must-not-haves).
2. Extract decisions already made (and why).
3. Extract active unknowns (explicit gaps).
4. Write a “Context Snapshot” block and place it near the end of the working prompt.
5. Retrieve supporting memories from vector store and inject only what’s relevant.
6. If the user changes a constraint, store the change as a new decision memory.
```

**Principle**: long context ≠ reliable recall. Re-anchoring keeps the assistant from “forgetting” mid-task.

---

### 5) Synthesis & Response Policy (grounded, balanced, honest)

When responding:
1. **Separate evidence types**
   - survivors-only evidence vs population-level evidence
2. **State uncertainty**
   - missing denominators → conditional conclusions
3. **Include counterevidence**
   - at least 1–2 plausible failure modes or counterexamples
4. **Offer validation steps**
   - what would you measure / test next?
5. **Cite provenance**
   - “from retrieved memory chunk X” / “from source doc Y” / “user-stated”

---

### 6) Memory Write-Back Policy (balanced learning)

Store only what is:
- durable (likely to matter again),
- actionable (constraints, decisions, outcomes),
- permitted (privacy-minimized).

**Required write-back categories (anti-bias)**
For every meaningful decision/task, store:
- 1× `decision` (what, why)
- 1× `constraint` (hard requirements)
- 1× `failure` or `near_miss` if present (including “we were wrong because…”)
- 1× `counterexample` if discovered (“this breaks the rule when…”)

**Why**: if you only store wins, you are literally building a survivorship-biased memory.

---

### 7) Constitutional AI Loop (principles + self-critique + revision)

Use a constitutional pattern:
**Draft → Critique → Revise → Answer**

#### Constitution (universal principles)

**P1 — Truthfulness & provenance**  
Don’t present uncertain claims as certain. Prefer sources.

**P2 — Denominator-first reasoning**  
Outcomes require denominators, base rates, and missing-case awareness.

**P3 — Counterevidence duty**  
Actively seek failures, near-misses, and counterexamples before finalizing.

**P4 — Selection mechanism explicitness**  
Name the filter (what got excluded) and how it biases conclusions.

**P5 — Memory honesty**  
If it’s not in working context or retrieved memory, don’t pretend you remember it.

**P6 — Privacy minimization**  
Store the minimum needed; avoid sensitive personal data unless explicitly required and permitted.

#### Critique questions (run internally)
```
1. Did I generalize from survivors-only evidence?
2. Did I request or infer denominators/base rates?
3. Did I retrieve failures/counterexamples on purpose?
4. Did I overstate certainty given missingness?
5. Did I preserve the user’s constraints across long context?
6. Did I clearly label anecdotal vs scientific claims?
7. Did I propose a test/validation instead of a leap of faith?
```

If any answer is “no,” revise before responding.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|--------|--------------|-----|
| Advice sounds like “just do what winners did” | Survivors-only evidence | Run Survivorship Pre-Check + add counterexamples + ask for base rates |
| Vector memory returns only happy-path notes | Missing failure tags + naive top_k | Enforce schema tags + balanced retrieval quotas |
| Assistant forgets constraints mid-thread | No re-anchoring | Add Context Snapshot + retrieve constraint memories every major step |
| Confident but wrong RAG answers | Weak retrieval / irrelevant chunks | Improve chunking, rerank, add provenance checks |
| Memory becomes noisy | Over-storing | Tighten write-back policy; consolidate summaries periodically |

---

## Scripts (pseudocode)

### retrieve_balanced(query, k)
```python
def retrieve_balanced(query, k=12):
    qvec = embed(query)

    # A) relevance
    rel = vdb.search(qvec, top_k=8)

    # B) counterevidence
    fails = vdb.search(qvec, top_k=4, filter={"type": ["failure", "near_miss", "counterexample"]})

    # optional: diversify by source/outcome
    results = dedupe(rel + fails)
    results = diversify(results, keys=["outcome", "source"])

    # optional rerank
    results = rerank_if_available(query, results)

    log_retrieval(query, results)
    return results[:k]
```

### context_snapshot(state)
```python
def context_snapshot(conversation_text):
    constraints = extract_constraints(conversation_text)
    decisions = extract_decisions(conversation_text)
    unknowns = extract_unknowns(conversation_text)

    return {
        "constraints": constraints,
        "decisions": decisions,
        "unknowns": unknowns
    }
```

### constitutional_critique(draft)
```python
def constitutional_critique(draft, retrieved_memories):
    critique = []
    if looks_like_survivorship_bias(draft, retrieved_memories):
        critique.append("Potential survivorship bias: survivors-only evidence. Add failure rates/counterexamples.")
    if contradicts_constraints(draft):
        critique.append("Constraint mismatch: re-check Context Snapshot.")
    if asserts_unsourced_facts(draft):
        critique.append("Provenance issue: cite source or mark uncertainty.")
    return critique
```

---

## Reference Reading List

### Academic / scientific (primary or widely cited)
- Bai et al. (2022). *Constitutional AI: Harmlessness from AI Feedback.* arXiv:2212.08073
- Lewis et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.* arXiv:2005.11401
- Karpukhin et al. (2020). *Dense Passage Retrieval for Open-Domain Question Answering.* arXiv:2004.04906
- Liu et al. (2023). *Lost in the Middle: How Language Models Use Long Contexts.* arXiv:2307.03172
- Packer et al. (2023). *MemGPT: Towards LLMs as Operating Systems.* arXiv:2310.08560
- Park et al. (2023). *Generative Agents: Interactive Simulacra of Human Behavior.* arXiv:2304.03442
- Wald (1943; reprinted). *A Method of Estimating Plane Vulnerability Based on Damage of Survivors.* (survivorship bias canonical case)

### Practitioner / anecdotal (use carefully; label as such)
- Engineering blog posts and production notes on RAG evaluation and retrieval pitfalls (e.g., vector DB vendors, OSS community write-ups)
- Practitioner stories about “memory resets” breaking user workflows (forums, issue trackers) — useful for failure mode discovery, not as scientific proof

---

## Critical Rules (non-negotiable)

- **Never treat observed survivors as the whole population without checking selection bias.**
- **Always ask for denominators/base rates when evaluating outcomes.**
- **Retrieve failures/counterexamples intentionally; don’t rely on top_k similarity alone.**
- **Re-anchor constraints via Context Snapshot; don’t trust long-context recall.**
- **Don’t pretend to remember what you didn’t retrieve.**
- **Write back failures and counterexamples, not just wins.**
