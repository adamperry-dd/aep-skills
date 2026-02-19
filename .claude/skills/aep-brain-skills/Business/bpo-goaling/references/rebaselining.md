# Rebaselining Reference

## Table of Contents
1. [Time-Based Triggers](#time-based-triggers)
2. [Systemic & External Triggers](#systemic--external-triggers)
3. [KPI Forgiveness](#kpi-forgiveness)
4. [Rebaseline Process](#rebaseline-process)

---

## Time-Based Triggers

KPI goals are **reviewed for rebaseline needs at the end of each quarter**.

A rebaseline review does not automatically result in goal adjustments—it's an evaluation checkpoint.

---

## Systemic & External Triggers

Goals *may* be rebased outside regular cadence when these conditions occur:

### Data Methodology & Logic Adjustments

| Trigger | Threshold |
|---------|-----------|
| Logic definition/calculation changes | 3+ weeks of abnormal WoW changes |

**Examples:**
- Change in survey delivery methodology for TxDWR
- Revising Teammate (Tx) non/controllables included in TxFCR

### Performance Deviations & Market Shifts

| Trigger | Threshold |
|---------|-----------|
| Sustained movement in TxDWR, TxFCR, or QA Confidence | ±3% due to logic/workflow changes |
| Volume reallocations outside bi-annual network design | Causing network performance fluctuations |

**Example:** Shifting volume to lower-performing partner to address SLA headwinds

### Network & Partner Updates

| Trigger | Threshold |
|---------|-----------|
| New Partner onboarding | Affects benchmarks where Partner owns ≥10% of LOB/Pod volume |
| Existing Partner removal | Affects benchmarks where Partner owns ≥10% of LOB/Pod volume |
| Bi-annual network restructuring | Planned design exercises |

---

## KPI Forgiveness

Goals may be **forgiven** during intermittent periods where external factors impact KPI performance.

### Enterprise-Wide Changes

- New business priorities, CX policies, or regulatory updates affecting KPIs
- SLA deviations impacting service delivery (e.g., systemic delays affecting TxDWR)

### Forgiveness vs Rebaseline

| Scenario | Action |
|----------|--------|
| Temporary disruption (1-2 weeks) | Forgiveness—don't count against partner |
| Sustained impact (3+ weeks) | Evaluate for rebaseline |

---

## Rebaseline Process

### Step 1: Document the Trigger

Record which trigger category applies:
- Time-based (quarterly review)
- Logic/methodology change
- Performance deviation
- Volume reallocation
- Network change

### Step 2: Gather Updated Benchmarks

Request from NOE:
- Fresh teammate-level percentile data
- Updated lookback period analysis
- Impact assessment of the triggering event

### Step 3: Calculate New Targets

Apply standard methodology:
- DWR: P80 (active LOBs), P75 (passive)
- FCR, AHT: P75

### Step 4: Apply >4% Rule

Compare new targets against Partner Initiative:
- Gap >4%: Use Partner target with documented rationale
- Gap ≤4%: Use new benchmark

### Step 5: Create New Goal Walks

- Generate weekly walks from current state to new target
- Ensure proper direction (DWR/FCR up, AHT down)
- Validate 13 weeks per quarter

### Step 6: Upload and Audit

- Check for existing Goal IDs (avoid duplicates)
- Create Sigma upload CSV
- Document changes in Goals Workbook
- Communicate to affected partners

---

## Documentation Requirements

Every rebaseline must include:

1. **Trigger identification**: Which category and specific event
2. **Data evidence**: Before/after metrics showing impact
3. **Stakeholder approval**: PxS DRI and Goal Sponsors sign-off
4. **Partner communication**: Timeline and rationale shared with affected partners
5. **Audit trail**: Changes recorded in Goals Workbook with timestamps
