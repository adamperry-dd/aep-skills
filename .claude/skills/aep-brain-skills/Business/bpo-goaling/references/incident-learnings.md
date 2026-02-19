# Incident Learnings — H1 2026 Goal Data Crisis

**Date:** January 20, 2026  
**Resolution Time:** 13.5 hours  
**Scope:** 282 Goal IDs, 3,666 weekly targets

---

## Critical Discoveries

### 1. Workbook-Partner Values Can DECLINE While Initiative-Partner IMPROVES

**The Problem:**
- Initiative-Partner: 0.670 → 0.697 (UP ✓)
- Workbook-Partner: 0.683 → 0.654 (DOWN ✗)
- Sigma used Workbook-Partner → goals walked WRONG direction

**The Rule:**
**ALWAYS check Initiative-Partner FIRST.** Document which source was used for every goal.

---

### 2. Merged Channels Are REAL (Not Optional Logic)

**DxDirect & PPod** and **DxNL/TS**: One Initiative row creates TWO Goal IDs.

**What Happened:**
- 27 of 47 "unknown source" goals were missed because merged channel logic wasn't applied
- Searching for "Dx Direct and Payments-DxChat-TaskUs" failed because Initiative file shows "DxDirect & PPod"

**The Fix:**
```python
MERGED_LOBS = {
    'Dx Direct and Payments': ['DxChat', 'DxPhone'],
    'Non-Live/App Troubleshooting': ['DxChat', 'DxPhone']
}
```
Create entries for BOTH queues from ONE source row.

---

### 3. Goal ID Parsing MUST Handle "/" and Multiple "-"

**The Problem:**
- "Non-Live/App Troubleshooting" split incorrectly on "/"
- Parsed as: "Non" | "Live/App Troubleshooting-DxChat" (WRONG)
- Should be: "Non-Live/App Troubleshooting" | "DxChat" (RIGHT)

**The Fix:**
- Split on `---_` FIRST (reliable separator)
- RSPLIT from right to extract partner (always single token)
- Special-case handling for LOBs containing "/"

See `scripts/parse_goal_id.py` for implementation.

---

### 4. Interpolation Is REQUIRED (Not Optional)

**The Problem:**
- Initiative file often has `None` for Week 1 (12/29/2025)
- Comparing None to 0.721 → "NOT_FOUND" instead of "EXACT"

**The Fix:**
Apply interpolation BEFORE any comparison:
```python
if metric in ['DWR', 'FCR']:
    week_1 = week_2 - 0.003  # Percentage: 0.3 points worse
elif metric == 'AHT':
    week_1 = week_2 + 0.3    # Minutes: 0.3 minutes longer
```

Week 1 should always show a starting point that IMPROVES to Week 2.

---

## Issues Found

| Issue | Count | Impact |
|-------|-------|--------|
| Duplicate rows (total) | 9,882 | Data integrity compromised |
| Missing Goal IDs | 118 | 76% of H1-26 goals missing |
| CxChat DWR never defined | 16 | Goals couldn't be created |
| Mis-entered values (whole vs decimal) | 21 | 82 instead of 0.82 = 8200% |
| Goals walking wrong direction | 7 | Should UP, went DOWN |
| Unknown source goals | 47 | Couldn't trace to Initiative/Workbook |

---

## Root Causes (Without Blame)

1. **No duplicate prevention in Sigma** - System allows same (Goal ID + Date)
2. **Incomplete upload validation** - Missing goals went undetected until WBR reporting
3. **Format ambiguity** - Single column for both percentages (0.82) and minutes (8.43)
4. **Manual extraction complexity** - Partner Initiative files have varying formats
5. **Insufficient documentation** - Current NOE SOP lacks validation steps
6. **Timing gaps** - Goals uploaded during first reporting week, not beforehand

---

## Prevention Measures Implemented

### Within PxS Control (Completed)

✅ **AI Prompts for SOP Maintenance**
- PxS BPO Goaling Methodology SOP Editor
- NOE Goals Management Sigma SOP - Improved

✅ **Pre-Upload Validation Checklist**
- Check for existing Goal IDs (prevent overwriting)
- Validate source file structure
- Apply interpolation before extraction
- Verify expected counts (282 Goal IDs, 3,666 rows)

✅ **Source Hierarchy Rules Documented**
- Initiative-Partner > Workbook-Partner > Workbook-Overall
- Document which source used for each goal

✅ **>4% Threshold Rule Codified**
- Statistical justification (SE = √(p(1-p)/n))
- Industry sources (Amazon, AmEx, Capital One, GE Six Sigma)

### Requires Cross-Functional Support (Recommended)

⚠️ **P0 - Critical:**
- Implement unique constraint in Sigma on (Goal ID + Date)
- Add format validation (decimal detection for Goal Values)

⚠️ **P1 - High:**
- Create standardized Partner Initiative template
- Automated goal count verification (expected vs actual)
- Earlier upload deadline (2 weeks before first reporting)

⚠️ **P3 - Low:**
- Clean up historical 7,994 duplicate rows

---

## Expected Counts (For Validation)

| Dimension | Count |
|-----------|-------|
| LOB/Partner Combinations | 47 |
| Metrics (DWR, FCR, AHT) | 3 |
| Quarters (Q1 + Q2) | 2 |
| **Total Goal IDs** | **282** (47 × 3 × 2) |
| Weeks per Quarter | 13 |
| **Total Weekly Targets** | **3,666** (282 × 13) |
| BPO Partners | 8 (Alorica, CP360, Concentrix, MZA, TaskUs, Telus, TTec, VXI) |

---

## Scope (In vs Out)

### In Scope (H1 2026)
- Consumer: CxChat, CxPhone (Mainline, VIP, Spanish, Specialized Pod)
- Dasher: DxChat, DxPhone (Mainline, VIP, Spanish, Direct & Payments, NL/TS)

### Out of Scope
- Dasher Shop & Deliver (DSD)
- Local Advocate DWR
- Consumer New Business Verticals (CxNBV)
- CSS/SaaS, Supervisor Adherence, LA Adherence
- DashPass Cancels Adherence
- Automated Quality Assurance (AQA)

---

## Common Issues → Solutions

### "Unknown Source" Goals

**Causes:**
1. Merged channel logic not applied
2. LOB name mismatch (Initiative vs Sigma naming)
3. Goal ID parsing failed
4. Interpolation not applied before comparing

**Solutions:**
1. Check merged channels FIRST (DxDirect, DxNL/TS)
2. Apply LOB name mappings (see naming-conventions.md)
3. Use corrected parsing (rsplit from right)
4. Apply interpolation BEFORE comparing first/last values

### Goals Walking Wrong Direction

**Cause:** Used Workbook-Partner instead of Initiative-Partner

**Solution:**
- ALWAYS check Initiative-Partner first
- Verify direction: DWR/FCR UP, AHT DOWN
- Document which source was used

### Duplicates in Sigma

**Cause:** No unique constraint allows duplicate (Goal ID + Date)

**Solution:**
- Pre-upload validation: Check for existing (Goal ID + Date)
- Delete duplicates before uploading
- Recommend Data Eng implement constraint

---

## Date Mappings (Q1/Q2 2026)

### Q1 2026 (13 weeks)

| Week | Date | Initiative Column |
|------|------|-------------------|
| 1 | 2025-12-29 | 67 |
| 2 | 2026-01-05 | 68 |
| 3 | 2026-01-12 | 69 |
| ... | ... | ... |
| 13 | 2026-03-23 | 79 |

### Q2 2026 (13 weeks)

| Week | Date | Initiative Column |
|------|------|-------------------|
| 1 | 2026-03-30 | 80 |
| 2 | 2026-04-06 | 81 |
| 3 | 2026-04-13 | 82 |
| ... | ... | ... |
| 13 | 2026-06-22 | 92 |

All dates are **Monday start dates** in **YYYY-MM-DD** format.

---

## References

- **H1-26 Goal Data Incident Post-Mortem** (January 21, 2026)
- **P0-1 DWR Fixes Required.csv** (7 goals needing correction)
- **Goal Audit FINAL AllSources.csv** (282 goals audited)
- **PxS BPO Goaling Methodology SOP**
- **NOE Goals Management Sigma SOP**

---

**Key Takeaway:** The incident revealed that our source hierarchy and validation processes needed codification. This reference captures those learnings to prevent recurrence in H2 2026, H1 2027, and beyond.
