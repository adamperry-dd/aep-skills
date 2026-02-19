# Adam Perry's Working Glossary

**Purpose:** Living document of working definitions, DoorDash-specific terminology, and conversational shorthand.  
**Location:** `/home/claude/references/adam-glossary.md`  
**Last Updated:** 2026-01-25

---

## DoorDash Metrics & KPIs

### TxFCR (Teammate First Contact Resolution)
- **Working Definition:** Teammate-level first contact resolution rate
- **Formal vs Working:** "TxFCR" is conversational shorthand; formally "Teammate First Contact Resolution"
- **Context:** Individual agent metric (vs aggregate Partner-level FCR)
- **Direction:** UP is better (higher = better quality)
- **Measurement Level:** Per-agent/teammate
- **2024 Performance:** 92.69% → 95.56% (exceeded 95.00% goal)
- **Related:** FCR (aggregate level)

### FCR (First Contact Resolution)
- **Working Definition:** First Contact Resolution at aggregate/Partner level
- **Context:** Aggregate metric across teams/partners (vs individual TxFCR)
- **Direction:** UP is better
- **Measurement:** P75 for goaling
- **Related:** TxFCR (teammate level)

### DWR (Did We Resolve)
- **Working Definition:** Customer satisfaction survey metric
- **Formal:** Post-contact survey asking "Did we resolve your issue?"
- **Context:** Customer-reported resolution success
- **Direction:** UP is better (higher = more satisfied customers)
- **Measurement:** P80 for actively managed LOBs
- **Goal Walk:** Must walk UP over 13 weeks

### AHT (Average Handle Time)
- **Working Definition:** Average time to handle a support case
- **Context:** Efficiency metric for support interactions
- **Direction:** DOWN is better (faster = more efficient)
- **Measurement:** P75 for goaling
- **Goal Walk:** Must walk DOWN over 13 weeks
- **Trade-off:** Balance with quality metrics (E2A)

### TxAHT (Teammate Average Handle Time)
- **Working Definition:** Per-teammate handle time metric
- **Context:** Individual-level version of AHT
- **Direction:** DOWN is better
- **Adam's Work:** Led dashboard launch with SOPs and Sigma integration
- **Related:** AHT (aggregate)

### MTR (Lateral Transfers)
- **Working Definition:** Measure of transfers between support channels/queues
- **Context:** Customer friction metric (handoffs create poor experience)
- **Direction:** DOWN is better (fewer handoffs = smoother resolution)
- **2024 Achievement:** 21 bps reduction via targeted partner initiatives

### Repeat Contact
- **Working Definition:** Customer contacting support again about same issue
- **Context:** Quality failure metric (indicates first contact didn't resolve)
- **Direction:** DOWN is better
- **2024 Achievement:** 5.15% → 3.52% (32% improvement)

### Utilization
- **Working Definition:** Agent productive time percentage
- **Context:** Workforce efficiency metric (time on cases vs available time)
- **Direction:** Higher is generally better (but quality matters too)

### QA (Quality Assurance)
- **Working Definition:** Quality assessment scores from manual review
- **Context:** Human evaluation of support interactions

### AQA (Automated Quality Assurance)
- **Working Definition:** Automated quality scoring
- **Context:** AI/rules-based quality evaluation without human review

### E2A (Effort to Accuracy)
- **Working Definition:** Metric balancing speed vs quality
- **Context:** Trade-off between fast handling (low effort) and accurate resolution
- **Adam's Stance:** Advocated for accuracy over speed in Chat workflow project

---

## DoorDash Organizational Terms

### BPO (Business Process Outsourcing)
- **Working Definition:** External vendor partners providing support services
- **Adam's Partners:** Alorica, TaskUs, Concentrix, CP360, TTec, Teleperformance, VXI, MZA
- **Count:** 8+ partners managed
- **Adam's Role:** BPO Partner Success Manager

### LOB (Line of Business)
- **Working Definition:** Product/service vertical with distinct support needs
- **Format:** [Customer Type][Channel] (e.g., CxPhone, DxChat)
- **Customer Types:**
  - Cx = Consumer
  - Dx = Dasher
- **Channels:**
  - Phone, Chat, etc.
- **Examples:** CxPhone, DxChat, CxChat, DxPhone
- **LOB × Queue:** 18+ combinations that Adam tracks

### Queue
- **Working Definition:** Specific support routing category within LOB
- **Types:**
  - **Mainline:** General/standard queue
  - **VIP:** High-value customer queue
  - **Specialized:** Specific issue types or customer segments

### Partner
- **Working Definition:** BPO vendor providing support services
- **Usage:** Used interchangeably with "BPO Partner" or "vendor"
- **Adam's Partners:** See BPO list above

### PxS (Partner Success)
- **Working Definition:** Partner Success team (Adam's team)
- **Function:** Manage BPO partner relationships, performance, and accountability
- **Team Size:** Small team within CXI organization

### CXI (Customer Experience Innovation)
- **Working Definition:** Customer Experience Innovation organization
- **Context:** Broader org that PxS reports into
- **Adam's Position:** Within CXI → 111 Support → PxS

### 111 Support
- **Working Definition:** Support organization designation at DoorDash
- **Context:** Adam's department within CXI

### Tx (Teammate)
- **Working Definition:** Individual support agent/representative
- **Usage:** TxFCR, TxAHT (teammate-level metrics)
- **Context:** Person handling customer support interactions

---

## Goaling & Performance Management

### CCG (Customer-Centric Goaling)
- **Working Definition:** Goal-setting methodology Adam developed in 2024
- **Innovation:** Shifts from teammate-level to Partner-level aggregated goals
- **Benefits:** Fairness, scalability, customer-centric alignment
- **Validation:** NOE's independent Q4 approach matched Adam's methodology
- **Status:** Shaping 2025 KPI goals

### Initiative File
- **Working Definition:** Primary source file containing Partner performance targets
- **Context:** Official source of truth for goal setting
- **Usage:** Referenced when creating Sigma upload CSVs

### Workbook
- **Working Definition:** Secondary/supplementary goal source file
- **Context:** Contains additional targets not in Initiative file
- **Relationship:** Supplement to Initiative file, not replacement

### Sigma
- **Working Definition:** DoorDash's data warehouse and analytics platform
- **Adam's Usage:** Where goals are uploaded, tracked, and reported
- **Integration:** Sigma-Anchored Smart Sheets approach for KPI tracking

### Goal ID
- **Working Definition:** Unique identifier for a goal in Sigma
- **Format:** `BPO-{Quarter}-{Year}-{Interval}-{Level}-{Metric}---_{Queue}-{LOB}-{Partner}`
- **Example:** `BPO-Q1-2026-Weekly-Team-DWR---_Mainline-CxPhone-Alorica`
- **Critical:** Must be exactly correct for Sigma to ingest properly

### Weekly Walk
- **Working Definition:** 13-week progression of goal targets
- **Mechanism:** Goals step up (or down) incrementally over 13 weeks
- **Direction Rules:**
  - DWR/FCR: Walk UP (improvement = higher %)
  - AHT: Walk DOWN (improvement = lower time)
- **Purpose:** Gradual improvement targets vs step-function changes

### Rebaselining
- **Working Definition:** Adjusting goal targets mid-period based on new reality
- **Trigger:** Original targets become unachievable due to external factors
- **Process:** Recalculate walks from new baseline performance
- **Governance:** Requires justification and approval

### Unknown Source
- **Working Definition:** Sigma goal error when source Initiative/Workbook unclear
- **Cause:** Missing or ambiguous mapping in goal upload CSV
- **Fix:** Verify which source file contains the target

### Wrong Direction
- **Working Definition:** Sigma goal error when metric walks opposite of intended
- **Examples:**
  - DWR walking DOWN (should walk UP)
  - AHT walking UP (should walk DOWN)
- **Fix:** Verify goal logic and upload CSV direction

---

## Technical & Project Terms

### TOSA (Training Operations Support Analyst)
- **Working Definition:** Training support role
- **Context:** Adam had exposure to this in 2020
- **Function:** Support frontline agent training and development

### LMS (Learning Management System)
- **Working Definition:** Platform for training content delivery
- **Adam's Work:** Led Cornerstone LMS transition, migrated 500+ lessons, eliminated 1800+ redundant items
- **Impact:** $100K+ savings by enabling in-house content transformation

### MCP (Model Context Protocol)
- **Working Definition:** Standard protocol for AI tool communication
- **Context:** Used with Claude Code, Skills, and integrations
- **Adam's Setup:** 49/50 skills installed across multiple domains

### Jira Intake Process
- **Working Definition:** Structured workflow for PxS team collaboration
- **Integration:** Jira + Slack for request tracking
- **Volume:** 350+ tickets processed since Q2 2024
- **Impact:** Scalability and efficiency for team workflows

---

## Adam's Working Vocabulary

### "Spiraling"
- **Working Definition:** Getting stuck in circular reasoning or infinite loops
- **Context:** Trigger phrase for lorazepam-protocol
- **Related:** "Going in circles", "circular reasoning"
- **Usage:** "You're spiraling" = stop and verify data before continuing

### "BLUF" (Bottom Line Up Front)
- **Working Definition:** Lead with conclusion/recommendation first
- **Format:**
  1. Decision/headline
  2. Why it matters
  3. Recommendation + owner + timing
  4. Risks/dependencies
  5. Supporting details
- **Update 2026-01-25:** Now optional unless specifically requested (per recent_updates in userMemories)

### "VP-grade output"
- **Working Definition:** Executive-quality deliverable standards
- **Clarification:** Output quality standard, NOT Adam's actual level
- **Requirements:**
  - Tradeoffs clearly stated
  - Costs and resourcing
  - Stakeholder map
  - Decision ask
  - Could be forwarded to VP tomorrow

### "Truth hygiene"
- **Working Definition:** Rigorous fact-checking and assumption labeling
- **Format:**
  - [VERIFIED] = Confirmed from source
  - Assumption: = Inference/extrapolation
  - [UNKNOWN - DO NOT INVENT] = Missing data
- **Principle:** Never fabricate unknown information

### "Red-team"
- **Working Definition:** Identify failure modes and second-order effects
- **Requirements:**
  - 1-2 likely failure modes
  - Gaming/incentive risks (especially for vendor scorecards)
  - Second-order effects (org behavior, morale, cost, customer impact)
- **Purpose:** Proactive risk identification

---

## Common Abbreviations

### Time Periods
- **EOY:** End of Year
- **Q1/Q2/Q3/Q4:** Quarters (Q1 = Jan-Mar, Q2 = Apr-Jun, Q3 = Jul-Sep, Q4 = Oct-Dec)
- **H1/H2:** Half-year (H1 = Jan-Jun, H2 = Jul-Dec)

### Meeting Types
- **WBR:** Weekly Business Review
- **QBR:** Quarterly Business Review
- **Cx WBR:** Customer Experience Bi-Weekly Business Review

### Document Types
- **PRD:** Product Requirements Document
- **SOP:** Standard Operating Procedure
- **KB:** Knowledge Base

### Teams/Functions
- **DE:** Data Engineering
- **BI:** Business Intelligence
- **NOE:** (Need to verify - appears in context of goaling methodology)

---

## How to Update This Glossary

### Adding New Terms
1. Determine appropriate category (Metrics, Org Terms, Technical, etc.)
2. Include:
   - Working Definition
   - Context (how/when it's used)
   - Direction (for metrics: UP vs DOWN)
   - Format/Examples
   - Related terms (cross-reference)
3. Distinguish formal vs conversational usage
4. Update "Last Updated" date at top

### Correcting Definitions
1. Update the definition
2. Note if significantly different from previous
3. Add context for why it changed
4. Update date at top

### When to Add
- New DoorDash terminology encountered
- Conversational shorthand Adam uses
- Formal definitions that differ from working usage
- Cross-team terms that need translation
- Acronyms that aren't self-evident

---

## Notes

- **Working vs Formal:** This glossary prioritizes how terms are used in practice over official definitions
- **Cross-References:** Related terms help understand metric relationships and hierarchy
- **Direction Matters:** For metrics, UP vs DOWN indicates success criteria
- **Context is Key:** Same acronym may mean different things in different contexts
- **Living Document:** Update as we encounter new terms or usage patterns
