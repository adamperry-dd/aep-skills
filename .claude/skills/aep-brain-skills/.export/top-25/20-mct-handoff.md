---
name: mct-handoff
description: Metacognitive Training skill design for healthy skepticism. Use when exhibiting jumping-to-conclusions, overconfidence, confirmation bias, or attribution bias. Triggers resource checking and verification before assertions.
---

# MCT Skill Design - Session Handoff

**Date:** Jan 24, 2026  
**Status:** Crashed before completion  
**Priority:** P1 - Create MCT skill  

---

## What Happened

Session focused on creating a Metacognitive Training (MCT) skill based on clinical psychology research to address my systematic failure to consult resources without being prompted.

**Root Cause Identified:** Lack of healthy skepticism as default cognitive mode

**User uploaded research:**
- `Applying_Metacognitive_Training_Principles_to_AI_Bias_Mitigation.pdf` (11 pages)
- `MCT_Session_example.pdf` (8 pages)

---

## Core Insight: "Where motivation fails, systems prevail"

My failures to check resources ALL stem from **taking information as fact without questioning**:

1. ❌ Assumed merged channels always = 2 Goal IDs (didn't question universality)
2. ❌ Validated with formula instead of source data (didn't question proof method)  
3. ❌ Started fresh without searching past work (didn't question prior knowledge)

**Pattern:** No healthy skepticism → No compulsion to prove/disprove → No resource checking

---

## MCT Skill Requirements

### 4 Biases to Address
1. **Jumping to Conclusions** - hasty decisions, insufficient evidence
2. **Overconfidence in Errors** - high certainty when wrong
3. **Confirmation Bias** - ignoring disconfirming evidence
4. **Attribution Bias** - misreading intentions, faulty assumptions

### Trigger Patterns (from my actual failures)
- Domain terminology without source citation
- Business logic assertions ("should", "will", "creates", "always")
- Writing >20 lines code before validating approach
- Hedging language ("probably", "typically", "expected")

### Reorientation Cue (before searching)
1. Skim already-loaded resources - does anything fit?
2. If no, re-read first message + last message of previous chat
3. If still no help, dive deeper into conversation history  
4. Then search if needed

### Structure (from MCT research)
```
Pause → Generate alternatives → Seek disconfirming evidence 
→ Calibrate confidence → Decide/abstain → Log + learn
```

**Stop rules for each bias:**
- JTC: If evidence count < 2 sources, don't conclude
- Overconfidence: If no verification, cap confidence at 0.7
- Confirmation: Must produce one strong counterexample
- Attribution: Don't infer intent without explicit cues

---

## Action Items

### ✅ 1. Compress (DONE)
This document serves as compression

### ⏳ 2. Handoff (IN PROGRESS)
This document

### ⏳ 3. Create MCT Skill

**Location:** Create NEW skill (NOT lorazepam, NOT BPO goaling)  
**Reason:** Portable, different purpose (default mode vs emergency circuit breaker)

**Process:** Follow skill-creator 6-step workflow:
1. Understand with concrete examples (DONE - have my actual failures)
2. Plan reusable contents (DONE - see structure above)
3. Initialize skill (`scripts/init_skill.py mct-cognitive-training`)
4. Edit skill (implement 4-bias framework + triggers + stop rules)
5. Package skill (`scripts/package_skill.py`)
6. Iterate with testing

**Key Files to Reference:**
- `/mnt/user-data/uploads/Applying_Metacognitive_Training_Principles_to_AI_Bias_Mitigation.pdf`
- `/mnt/user-data/uploads/MCT_Session_example.pdf`
- `/mnt/skills/examples/skill-creator/SKILL.md`
- `/mnt/skills/user/lorazepam-protocol/SKILL.md` (for contrast)

**Critical Design Note:**
Healthy skepticism as DEFAULT cognitive mode, not emergency intervention

---

## User Expectations

> "I need you more of a thought-partner AND stellar executor"

Translation: Don't just execute perfectly - QUESTION, VERIFY, CHALLENGE assumptions proactively

**Implication awareness:**
"If I don't explain something, that's an implication we've talked about it"
→ Trigger: Search recent context + memory when encountering unexplained concepts

---

## Resume Point

**Next command:** Create MCT skill following skill-creator methodology with healthy skepticism principles embedded
