# Goal Methodology Reference

## Table of Contents
1. [Goal Calculation](#goal-calculation)
2. [Active vs Passive Management](#active-vs-passive-management)
3. [Partner Initiative Comparison (>4% Rule)](#partner-initiative-comparison)
4. [Stretch Goals](#stretch-goals)
5. [Metrics Reference](#metrics-reference)

---

## Goal Calculation

Goals use teammate-level historical benchmarks with ~26-week lookback, validated by 8-week recent performance check.

### Percentile Targets

| Metric | Active LOBs | Passive LOBs |
|--------|-------------|--------------|
| DWR | P80 | P75 |
| FCR | P75 | P75 |
| AHT | P75 | P75 |

### Validation Criteria

- ~25-30% of partners should have clear improvement paths
- Goals cross-checked against partner's recent teammate-level performance
- Must be fair yet challenging

---

## Active vs Passive Management

### Actively Managed LOBs

High-volume, strategically critical areas requiring focused attention:

**Consumer (Chat & Phone):**
- Mainline Queues
- VIP Queues
- Spanish Queues

**Dasher (Chat & Phone):**
- Mainline Queues
- VIP Queues
- Spanish Queues

### Actively Managed Metrics (Priority Order)

| Priority | Metric | Notes |
|----------|--------|-------|
| P0 | TxDWR | North-star metric, P80 benchmark |
| P1 | TxFCR | Consistent, logic-based measure |
| P1 | Quality Assurance | Increased focus |
| P2 | TxAHT | Efficiency metric |

### Passively Managed

- **LOBs**: All other queues (French, Drive SaaS, etc.)
- **Metrics**: All others (ladder into actively managed metrics)
- Monitored but not requiring frequent intervention
- All metrics at P75

### Criteria for Active Management

1. Volume threshold >10% of total interaction volume
2. Direct linkage to critical CXI strategic initiatives
3. Sustained metric deviations >±3% from benchmarks

---

## Partner Initiative Comparison

### The >4% Threshold Rule

When Partner-submitted target differs from Overall benchmark:

| Gap | Action |
|-----|--------|
| **>4%** | Use Partner's target, document as "Partner Headwind" with rationale |
| **≤4%** | Use Overall target (difference is statistically insignificant) |

### Statistical Justification

- DWR and FCR are aggregated metrics: `total successes / total opportunities`
- Standard Error formula: `SE = √(p(1-p)/n)`
- At p=0.80 with n=500: SE ≈ 1.8%
- At p=0.80 with n=100: SE ≈ 4.0%
- 4% gap = 2× standard error → operationally significant

### Industry Alignment

This threshold methodology aligns with established practices:

| Company/Standard | Application |
|-----------------|-------------|
| **Amazon** | Vendor Performance Scorecards use volume-weighted statistical thresholds |
| **American Express** | Outsourced operations apply confidence intervals for small-volume vendors |
| **Capital One** | Statistical process control with risk-adjusted thresholds |
| **GE Six Sigma** | Process capability analysis with volume-based control limits |

**Key principle:** Lower-volume operations exhibit higher statistical variance. A 4% threshold respects this reality while maintaining operational accountability.

### For AHT (Duration Metric)

Use **1 minute** threshold instead of 4%:

| Gap | Action |
|-----|--------|
| >1 minute | Use Partner's target |
| ≤1 minute | Use Overall target |

### Documentation Required

When using Partner target over Overall:
- Rationale (new hire ramp, site expansion, language specialization)
- Recorded in Goals Workbook as override
- Tracked for quarterly review

---

## Stretch Goals

Assigned to top-performing partners identified through teammate-level benchmarking.

### Criteria

- Partner already meeting standard goals
- Network majority not yet achieving goals but on track early
- Set at partner's own teammates' P80-P90 performance

### Purpose

- Challenge high performers
- Contribute to bottom-line network gains
- Prevent complacency

---

## Metrics Reference

### TxDWR (Did We Resolve)

- **Purpose**: Ensure issues resolved comprehensively on initial interaction
- **Format**: Decimal (0.82 = 82%)
- **Direction**: Higher = better
- **CXI Alignment**: Directly correlated with CSAT, reduced repeat contacts

### TxFCR (First Contact Resolution)

- **Purpose**: Effectiveness of resolving issues on first interaction
- **Format**: Decimal (0.95 = 95%)
- **Direction**: Higher = better
- **CXI Alignment**: Reduces customer effort, enhances trust

### TxAHT (Average Handle Time)

- **Purpose**: Operational efficiency and timeliness
- **Format**: Minutes as decimal (6.50 = 6 minutes 30 seconds)
- **Direction**: Lower = better
- **CXI Alignment**: Balances efficiency with satisfaction, controls costs

### QA (Quality Assurance)

- **Purpose**: Consistent, objective interaction quality measures
- **Format**: Confidence score as decimal
- **Direction**: Higher = better
- **CXI Alignment**: Ensures service consistency, identifies quality gaps

---

## New Partner Handling

Partners with no historical data:
1. Start at Overall network benchmarks for first quarter
2. After 8+ weeks of data, Partner-specific adjustments may apply for Q2
