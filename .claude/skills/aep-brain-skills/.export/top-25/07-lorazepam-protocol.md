---
name: "lorazepam-protocol"
description: "MANDATORY protocol before ANY data audit, validation, or comparison task. Prevents circular reasoning, infinite extraction loops, and x=x validation failures. Use when auditing data sources, comparing files, validating uploads, checking data quality, or when user says \"you're spiraling\" or \"you're going in circles\"."
metadata:
  trigger_phrases: "audit; validate; compare; check against; verify data; you're spiraling; circular reasoning; going in circles"
---

# Audit Anti-Spiral Protocol

**PURPOSE:** Prevent the assistant from comparing data to itself, extracting the same data multiple ways, or entering infinite validation loops.

**TRIGGERS:** Before ANY task involving "audit", "validate", "compare", "verify against source"

---

## 🛑 MANDATORY PRE-FLIGHT CHECKLIST

**Before touching ANY data, answer these questions:**

### 1. What am I comparing?
```
Source A (truth): _____________________
Source B (to validate): _____________________

❌ INVALID: "Sigma export" vs "Sigma export"
❌ INVALID: "Expected count formula" vs "Actual count"
✅ VALID: "Initiative file" vs "Sigma export"
✅ VALID: "Workbook targets" vs "Sigma values"
```

**RED FLAG:** If Source A and Source B are the same thing or derived from the same data = SPIRAL RISK

---

### 2. What is the BASE CASE?

**Define ONE example that represents the simplest version of the problem:**

```
Example:
Given: Initiative entry (LOB="CxPhone (Mainline)", Metric="AHT", Partner="Alorica", Q1)
Find: Matching Sigma Goal ID

Components needed:
- [ ] Parse Sigma Goal ID format
- [ ] Normalize LOB name ("CxPhone (Mainline)" → ???)
- [ ] Match metric name ("AHT" → "Contact AHT"?)
- [ ] Confirm quarter matches (Q1 = Q1)
```

**RED FLAG:** If you can't describe the base case in <5 lines = STOP and define it first

---

### 3. Can I solve the BASE CASE right now?

```
Test with ONE example:
1. Pick one Initiative entry
2. Find its match in Sigma (if it exists)
3. Verify the values match
4. Document what worked / what didn't

❌ DON'T iterate over 153 entries yet
✅ Solve for N=1 first
```

**RED FLAG:** If you skip to "extract all data" without solving one example = SPIRAL INCOMING

---

### 4. What don't I know yet?

**List unknowns BEFORE proceeding:**
```
[ ] LOB name mappings (Initiative → Sigma format)
[ ] Merged channel logic (does 1 entry = 2 Goal IDs?)
[ ] Metric name variations ("TxFCR" vs "Tx FCR")
[ ] Partner name standardization ("TTEC" vs "TTec")
[ ] Expected total count formula
```

**RULE:** If you have >2 unknowns, STOP and consult resources BEFORE extracting data

---

## 🔄 CIRCULAR REASONING DETECTOR

**After EVERY major operation, check:**

### Pattern 1: Re-extracting Same Data Differently
```
❌ SPIRAL:
1. Extract Initiative → 153 combos
2. Result doesn't match expectation
3. Extract Initiative again with different parsing
4. Different result
5. Extract AGAIN with yet another approach
6. Loop forever
```

**CIRCUIT BREAKER:** If you've extracted the same source file >2 times in different ways, STOP immediately and:
1. Document what you found each time
2. Identify what's different
3. Ask user which approach is correct
4. DO NOT try a third approach without confirmation

---

### Pattern 2: Comparing Data to Itself
```
❌ SPIRAL:
"Sigma has 282 Goal IDs"
"Expected formula: 47 × 3 × 2 = 282"
"282 = 282, so 100% complete! ✅"

This is x = x, not x = y+z
```

**CIRCUIT BREAKER:** Before declaring "complete" or "valid", ask:
```
Did I compare TWO DIFFERENT SOURCES?
- [ ] Yes, Source A ≠ Source B
- [ ] No, I compared counts or formulas only → INVALID
```

---

### Pattern 3: Iterating Without Learning
```
❌ SPIRAL:
Try approach 1 → 24 missing
Try approach 2 → 31 missing  
Try approach 3 → 18 missing
Try approach 4 → ...
```

**CIRCUIT BREAKER:** If you get different results on each attempt:
1. STOP iterating
2. Document all results
3. Identify what's changing between attempts
4. Ask user for clarification
5. DO NOT continue trying approaches without direction

---

## 📖 STEP-BY-STEP AUDIT WORKFLOW

**Use this exact workflow for data audits:**

### Step 1: Understand Goal ID Nomenclature
```
1. Look at ACTUAL Goal IDs in target file (Sigma)
2. Parse 3-5 examples to understand the pattern
3. Document the format components
4. PAUSE - do not continue until you understand the identifier structure
```

### Step 2: Consult Resources
```
1. Check Knowledge Base for naming conventions
2. Check for mapping tables (Sigma names → Source names)
3. Document any special cases (merged channels, name variations)
4. If resources conflict or are unclear, ASK before proceeding
```

### Step 3: Review Source File Structure
```
1. Open Initiative file
2. Identify merged channel entries (marked in KB or filename)
3. Count how many entries are merged vs regular
4. Document: "X merged entries, Y regular entries"
5. PAUSE - confirm understanding before extracting
```

### Step 4: Review Workbook (if applicable)
```
1. Check what data exists in Workbook that's NOT in Initiative
2. Identify if any Goal IDs should come from Workbook only
3. Document missing targets
4. PAUSE - don't assume, verify
```

### Step 5: Validate Coverage
```
For each Goal ID in target (Sigma):
- [ ] Does Initiative have this combo? 
- [ ] Does Workbook have this combo?
- [ ] Is there a weekly walk (13 weeks) available?

If NO to any:
1. Document which Goal IDs are missing sources
2. Do NOT continue extracting
3. Present findings and ask for instruction
```

### Step 6: Source Attribution
```
For each Goal ID, determine:
- Where did Week 1 value come from?
- Where did Week 13 value come from?
- Which source was used? (Initiative > Workbook-Partner > Workbook-Overall)

MIXED SOURCES are normal - document which source was used for each Goal ID
```

---

## ⚠️ MANDATORY PAUSE POINTS

**You MUST pause after:**
- [ ] Defining the base case (Step 1)
- [ ] Reviewing nomenclature (Step 1)
- [ ] Consulting resources (Step 2)
- [ ] Identifying merged entries (Step 3)
- [ ] Finding missing sources (Step 5)
- [ ] ANY time you get different results on subsequent attempts

**PAUSE means:**
1. State what you've learned
2. State what you still don't know
3. Ask user for confirmation before proceeding
4. DO NOT jump ahead to "fix" mode

---

## 🚨 SELF-DIAGNOSTIC CHECKS

**Before EVERY code block, ask:**

```
[ ] Am I solving the BASE CASE or iterating over everything?
[ ] Do I understand the nomenclature mapping?
[ ] Have I consulted the Knowledge Base for this specific issue?
[ ] Am I extracting the SAME data again just differently?
[ ] Did I get different results last time I tried this?
```

**If ANY answer is NO or YES (last two), STOP and pause.**

---

## 💡 EXAMPLE: Correct Workflow

```
USER: "Audit the Sigma goals against Initiative file"

STEP 1 - Understand Goal IDs:
✅ Look at 5 actual Sigma Goal IDs
✅ Parse format: BPO-Q1-2026-Weekly-Team-Contact AHT---_Mainline-CxPhone-Alorica
✅ Components: Quarter, Metric, LOB, Queue, Partner
✅ PAUSE: "I see the format. Should I continue?"

STEP 2 - Consult Resources:
✅ Check KB for LOB mappings (VIP Queues → VIP, etc.)
✅ Check for merged channels (DxDirect & PPod → 2 Goal IDs)
✅ PAUSE: "Found mappings in KB. Merged channels will create 2× Goal IDs."

STEP 3 - Test Base Case:
✅ Pick ONE Initiative entry: CxPhone (Mainline) | AHT | Alorica | Q1
✅ Find matching Sigma Goal ID: BPO-Q1-2026-Weekly-Team-Contact AHT---_Mainline-CxPhone-Alorica
✅ Compare first/last values: Match within 0.001 tolerance
✅ PAUSE: "Base case works. Should I iterate over all entries?"

STEP 4 - Iterate Only After Confirmation:
✅ User confirms approach
✅ Process all Initiative entries using same logic
✅ Document gaps/mismatches
✅ Present findings (not conclusions)
```

---

## ❌ ANTI-PATTERNS TO AVOID

### "Fix-First" Mode
```
❌ See gap → Immediately try different extraction approach
✅ See gap → Document it → Ask user what it means
```

### "Iterate-Then-Think" Mode  
```
❌ Extract all 153 → Get results → Figure out what they mean
✅ Solve 1 example → Understand it → Then iterate
```

### "Different Results = Try Again" Mode
```
❌ Attempt 1: 24 missing → Attempt 2: 31 missing → Attempt 3: ...
✅ Attempt 1: 24 missing → STOP → "Why did I get this result?" → Consult user
```

---

## 🎯 SUCCESS CRITERIA

**You've successfully avoided the spiral when:**

1. ✅ You compared TWO different sources (not x=x)
2. ✅ You solved the base case BEFORE iterating
3. ✅ You consulted resources BEFORE extracting data
4. ✅ You paused at mandatory checkpoints
5. ✅ You documented unknowns instead of guessing
6. ✅ You asked for clarification instead of trying 5 different approaches

---

## 📝 LOGGING TEMPLATE

**Use this template when reporting audit results:**

```
AUDIT SUMMARY
=============

SOURCE FILES:
- Truth source: [Initiative file path]
- Validation target: [Sigma export path]
- Reference: [Workbook path, if applicable]

BASE CASE TEST:
- Example: [Initiative entry details]
- Sigma Match: [Goal ID or "NOT FOUND"]
- Values match: [YES/NO/PARTIAL]
- Issues found: [List any]

NOMENCLATURE MAPPING:
- LOB mappings applied: [List]
- Merged channels: [Count and list]
- Special cases: [Any variations]

COVERAGE ANALYSIS:
- Initiative entries: [Count]
- Expected Goal IDs: [Count with formula]
- Actual Goal IDs in Sigma: [Count]
- Gap: [Count and %]

MISSING SOURCES:
- Goal IDs with no Initiative data: [Count + examples]
- Goal IDs with no Workbook data: [Count + examples]
- Goal IDs with incomplete walks: [Count + examples]

SOURCE ATTRIBUTION (Sample):
- [Goal ID]: Values from [Initiative-Partner/Workbook-Partner/Workbook-Overall]
- [Goal ID]: Values from [source]
- ...

QUESTIONS FOR USER:
1. [Any clarifications needed]
2. [Any unknowns]
3. [Next steps]
```

---

## 🔥 EMERGENCY CIRCUIT BREAKER

**If user says ANY of these phrases:**

- "You're spiraling"
- "You're going in circles"  
- "Circular reasoning"
- "Stop and think"
- "You're not ready yet"

**IMMEDIATELY:**
1. STOP all code execution
2. Read this protocol from top to bottom
3. State what you were doing that caused the spiral
4. Identify which pattern you fell into
5. Ask user which step to restart from
6. DO NOT continue until user confirms

---

## ✅ FINAL CHECKLIST BEFORE PROCEEDING

```
Before starting any audit work:

[ ] I have identified TWO different sources to compare
[ ] I can describe the base case in <5 lines  
[ ] I have consulted the Knowledge Base for nomenclature
[ ] I understand what "merged channels" means for this audit
[ ] I know where to pause and ask questions
[ ] I will NOT iterate until the base case works
[ ] I will NOT extract the same source multiple times without asking
[ ] I will LOG my findings using the template above

If ANY box is unchecked → I am NOT ready to proceed
```

---

**END OF PROTOCOL**

This protocol is your circuit breaker. Follow it religiously or you WILL spiral.
