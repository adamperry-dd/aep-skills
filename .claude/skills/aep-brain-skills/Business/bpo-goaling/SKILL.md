---
name: bpo-goaling
description: "BPO Partner goal management for DoorDash Partner Success (PxS). Use when: (1) Auditing Sigma goals against Initiative/Workbook source files, (2) Creating Sigma upload CSVs for new goal periods, (3) Troubleshooting unknown source or wrong direction goal issues, (4) Regoaling, rebaselining, or adjusting KPI target walks, (5) Checking if Goal IDs exist for a quarter/half, (6) Validating Partner Initiative targets against Overall benchmarks using the 4% threshold rule. Covers DWR, FCR, AHT metrics across Consumer/Dasher LOBs."
---

# BPO Goaling Skill

Manages BPO Partner KPI goals: auditing, creating uploads, troubleshooting, and rebaselining.

## File Intake Workflow

When triggered, request files based on the task:

| Task | Required Files |
|------|----------------|
| **Audit goals** | Initiative file (.xlsx), Workbook (.xlsx), Sigma export (.csv) |
| **Create upload CSV** | Initiative file, Workbook, Sigma export (to check existing Goal IDs) |
| **Troubleshoot goals** | Sigma export + Goal IDs in question, Initiative file |
| **Rebaseline** | Initiative file, Workbook, (optional) historical data |
| **Check Goal ID existence** | Sigma export for the target period |

### File Validation

After receiving files, extract and confirm:
1. **Period**: H1/H2 + year from filename or headers
2. **Column mappings**: Locate date headers (e.g., "12/29/25" = Week 1 Q1)
3. **Quarter boundaries**: Q1 cols vs Q2 cols (expect 13 weeks each)
4. **Partner list**: Extract from data rows
5. **Sheet structure**: Consumer (`Cx`) vs Dasher (`Dx`) sheets

## Core Workflows

### 1. Goal ID Existence Check

**Always run first** before creating new uploads.

```
1. Load Sigma export
2. Extract unique Goal IDs matching pattern: BPO-{Q1|Q2}-{YEAR}-Weekly-Team-*
3. Count by quarter and report:
   - Q1 Goal IDs found: X
   - Q2 Goal IDs found: X
   - Expected per quarter: 141 (varies by active LOBs)
4. If Goal IDs exist, STOP and confirm with user before overwriting
```

### 2. Audit Existing Goals

Compare Sigma values against source hierarchy.

**Source Priority (highest to lowest):**
```
1. Initiative-Partner  →  Partner's committed walk from Initiative file
2. Workbook-Partner    →  Partner-level target from Goals Workbook
3. Workbook-Overall    →  Overall LOB benchmark from Goals Workbook
```

**Audit Steps:**
1. Parse Goal IDs using `scripts/parse_goal_id.py`
2. For each Goal ID, extract first/last values from:
   - Sigma export
   - Initiative file (apply interpolation if Week 1 is None)
   - Workbook-Partner
   - Workbook-Overall
3. Match source using 0.001 tolerance
4. Calculate variance: `abs(source - sigma) / source`
5. Flag **HIGH** if variance > 2%
6. Verify walk direction:
   - DWR, FCR: Must walk UP (higher = better)
   - AHT: Must walk DOWN (lower = better)

### 3. Create Sigma Upload CSV

**Pre-flight checks:**
1. Run Goal ID existence check
2. Confirm no duplicates will be created
3. Validate source files have expected structure

**Extraction flow:**
1. Read Initiative file sheets (`Consumer- Cx`, `Dasher- Dx`)
2. For each section header (LOB/Metric), extract partner rows
3. Apply source hierarchy—use Initiative-Partner when available
4. Apply interpolation for missing Week 1 values (see scripts)
5. Handle merged channels: DxDirect & PPod, DxNL/TS create BOTH Chat and Phone entries
6. Format output:
   - Column 1: `Unique Goal ID`
   - Column 2: `Target Start Date` (YYYY-MM-DD, Monday dates)
   - Column 3: `Goal Values` (3 decimal places)

**Goal ID Format:**
```
BPO-{Quarter}-{Year}-Weekly-Team-{Metric}---_{LOB}-{Queue}-{Partner}
```

Example: `BPO-Q1-2026-Weekly-Team-DWR---_Mainline-DxChat-Alorica`

### 4. Troubleshoot Goals

Common issues and diagnostics:

| Symptom | Check | Solution |
|---------|-------|----------|
| "Unknown Source" | Merged channel logic applied? | See `references/naming-conventions.md` |
| | LOB name mapping correct? | Map Sigma LOB → Initiative LOB |
| | Goal ID parsing correct? | Use `scripts/parse_goal_id.py` |
| Goals walking wrong direction | Source hierarchy enforced? | Check Initiative-Partner first |
| | Using Workbook-Partner incorrectly? | Workbook can diverge from Initiative |
| Week 1 missing | Interpolation applied? | Run `scripts/interpolate.py` |
| Duplicates in Sigma | Pre-upload validation done? | Run `scripts/validate_upload.py` |

### 5. Rebaseline Workflow

Consult `references/rebaselining.md` for triggers. When rebaselining:

1. Document the trigger (time-based or systemic)
2. Pull fresh teammate-level benchmarks from NOE
3. Apply goal calculation methodology (see `references/methodology.md`):
   - DWR: P80 for actively managed LOBs
   - AHT, FCR: P75
4. Compare new targets against current using >4% rule
5. Create updated upload CSV with new walks
6. Maintain audit trail of changes

## References

| File | When to Read |
|------|--------------|
| `references/methodology.md` | Goal calculations, active vs passive LOBs, >4% threshold rule, industry sources |
| `references/rebaselining.md` | Rebaseline triggers, KPI forgiveness criteria |
| `references/naming-conventions.md` | LOB/Queue/Partner mappings, merged channel logic, Goal ID parsing |
| `references/incident-learnings.md` | H1 2026 crisis lessons, common issues, prevention measures, expected counts |

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/parse_goal_id.py` | Parse Goal ID into components (quarter, metric, LOB, queue, partner) |
| `scripts/interpolate.py` | Fill missing Week 1 values using 0.003/0.3 rules |
| `scripts/validate_upload.py` | Pre-upload validation for duplicates and format |

## Critical Rules

- **Always check Goal ID existence before creating uploads**
- **Apply source hierarchy strictly**: Initiative-Partner > Workbook-Partner > Workbook-Overall
- **Interpolate before comparing**: Week 1 often missing in Initiative file
- **Handle merged channels**: DxDirect and DxNL/TS create both Chat AND Phone entries from single row
- **Parse Goal IDs from right**: Use rsplit to handle LOBs with hyphens
- **Format values to 3 decimal places**: 0.820 not 0.82
- **Dates are Monday start dates**: YYYY-MM-DD format
- **Verify walk direction**: DWR/FCR UP, AHT DOWN
