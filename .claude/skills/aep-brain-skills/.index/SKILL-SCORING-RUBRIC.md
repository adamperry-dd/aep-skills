# Skill Scoring Rubric

**Purpose:** Identify top 25 critical skills for Claude Desktop (50 skill max)

## Scoring Dimensions (1-5 scale each)

### 1. Frequency of Use (Weight: 3x)
How often would this skill be invoked in typical work?

| Score | Criteria |
|-------|----------|
| 5 | Daily use - core to every session |
| 4 | Weekly use - regular workflow component |
| 3 | Bi-weekly - periodic but predictable need |
| 2 | Monthly - occasional specialized task |
| 1 | Rare - edge case or one-off situations |

### 2. Breadth of Application (Weight: 2x)
How many different use cases does this skill serve?

| Score | Criteria |
|-------|----------|
| 5 | Universal - applies across all work domains |
| 4 | Multi-domain - useful in 3+ work areas |
| 3 | Dual-domain - serves 2 distinct purposes |
| 2 | Single-domain - one specific area |
| 1 | Niche - very narrow application |

### 3. Native Gap Fill (Weight: 2x)
Does this provide guidance Claude doesn't have natively?

| Score | Criteria |
|-------|----------|
| 5 | Critical - addresses known Claude weakness/blindspot |
| 4 | Significant - specialized methodology not in training |
| 3 | Moderate - enhances existing capability notably |
| 2 | Minor - slight improvement over baseline |
| 1 | Redundant - Claude does this well without guidance |

### 4. Quality of Implementation (Weight: 1x)
How well-developed is the skill content?

| Score | Criteria |
|-------|----------|
| 5 | Excellent - comprehensive, actionable, tested |
| 4 | Good - solid guidance with clear workflows |
| 3 | Adequate - useful but could be improved |
| 2 | Basic - minimal guidance, needs development |
| 1 | Stub - placeholder or incomplete |

### 5. VP/Leadership Alignment (Weight: 2x)
Does this align with executive-level work patterns?

| Score | Criteria |
|-------|----------|
| 5 | Core executive function - strategy, decisions, communication |
| 4 | High leadership value - team, stakeholder, planning |
| 3 | Professional utility - general knowledge work |
| 2 | Technical support - implementation detail |
| 1 | Entry-level task - not leadership-relevant |

---

## Scoring Formula

**Total Score = (Frequency × 3) + (Breadth × 2) + (Gap Fill × 2) + (Quality × 1) + (VP Align × 2)**

**Maximum possible: 50 points**

## Score Interpretation

| Range | Tier | Action |
|-------|------|--------|
| 40-50 | **Essential** | Must include in top 25 |
| 30-39 | **High Value** | Include if space permits |
| 20-29 | **Moderate** | Consider for extended set |
| 10-19 | **Low Priority** | Exclude from core set |
| 1-9 | **Exclude** | Remove or archive |

---

## Scoring Matrix

### Core Skills (10)

| Skill | Freq | Breadth | Gap | Quality | VP | **Total** |
|-------|------|---------|-----|---------|----|----|
| knowledge-verification-protocol | 5 | 5 | 5 | 5 | 5 | **50** |
| adam-perry-onboarding | 5 | 5 | 5 | 4 | 5 | **48** |
| lorazepam-protocol | 4 | 4 | 5 | 4 | 4 | **42** |
| context-saver | 4 | 4 | 4 | 4 | 4 | **40** |
| handoff | 3 | 4 | 4 | 4 | 3 | **35** |
| session-memory | 3 | 4 | 4 | 3 | 3 | **33** |
| scientific-brainstorming | 3 | 4 | 4 | 4 | 4 | **37** |
| knowledge-distillation | 4 | 4 | 3 | 4 | 4 | **38** |
| mct-handoff | 3 | 3 | 5 | 3 | 4 | **35** |
| anti-survivorship-memory | 3 | 3 | 5 | 4 | 4 | **37** |

### Data & Analytics Skills (17)

| Skill | Freq | Breadth | Gap | Quality | VP | **Total** |
|-------|------|---------|-----|---------|----|----|
| python-data-visualization | 4 | 4 | 3 | 5 | 3 | **37** |
| exploratory-data-analysis | 4 | 4 | 4 | 5 | 4 | **42** |
| senior-data-scientist | 3 | 3 | 3 | 4 | 3 | **31** |
| statsmodels | 2 | 2 | 2 | 3 | 2 | **20** |
| data-storytelling | 4 | 4 | 4 | 4 | 5 | **42** |
| grafana-dashboards | 2 | 2 | 3 | 3 | 3 | **24** |
| kpi-dashboard-design | 3 | 3 | 4 | 3 | 5 | **36** |
| geopandas | 1 | 1 | 2 | 3 | 1 | **14** |
| networkx | 1 | 2 | 2 | 3 | 2 | **17** |
| anndata | 1 | 1 | 3 | 3 | 1 | **15** |
| neurokit2 | 1 | 1 | 3 | 3 | 1 | **15** |
| deeptools | 1 | 1 | 3 | 3 | 1 | **15** |
| vector-index-tuning | 2 | 2 | 4 | 3 | 2 | **24** |
| tensorboard | 2 | 2 | 2 | 3 | 2 | **20** |
| model-compression | 1 | 1 | 3 | 3 | 1 | **15** |
| hypogenic | 2 | 2 | 4 | 3 | 3 | **26** |
| google-analytics | 2 | 2 | 2 | 3 | 3 | **22** |

### Development Skills (13)

| Skill | Freq | Breadth | Gap | Quality | VP | **Total** |
|-------|------|---------|-----|---------|----|----|
| systematic-debugging | 3 | 4 | 4 | 4 | 2 | **33** |
| query-writing | 3 | 3 | 2 | 4 | 3 | **29** |
| schema-exploration | 2 | 3 | 3 | 3 | 2 | **24** |
| sql-optimization-patterns | 2 | 2 | 3 | 4 | 2 | **24** |
| dbt-transformation-patterns | 2 | 2 | 4 | 4 | 2 | **26** |
| n8n-code-javascript | 2 | 2 | 4 | 3 | 2 | **24** |
| n8n-workflow-patterns | 2 | 2 | 4 | 3 | 2 | **24** |
| agent-builder | 3 | 3 | 4 | 4 | 3 | **33** |
| artifact-builder | 3 | 3 | 3 | 4 | 2 | **29** |
| claude-d3js-skill-main | 2 | 2 | 3 | 3 | 2 | **22** |
| docstring | 2 | 2 | 1 | 3 | 1 | **16** |
| move-code-quality-skill-main | 2 | 2 | 2 | 3 | 2 | **20** |
| optimizing-attention-flash | 1 | 1 | 3 | 3 | 1 | **15** |

### Business Skills (12)

| Skill | Freq | Breadth | Gap | Quality | VP | **Total** |
|-------|------|---------|-----|---------|----|----|
| bpo-goaling | 4 | 3 | 5 | 4 | 5 | **42** |
| ceo-advisor | 3 | 4 | 4 | 4 | 5 | **40** |
| product-manager-toolkit | 3 | 4 | 3 | 4 | 5 | **38** |
| executing-plans | 4 | 4 | 4 | 4 | 5 | **42** |
| plan-writing | 4 | 4 | 3 | 4 | 5 | **40** |
| market-research-reports | 3 | 3 | 3 | 4 | 5 | **36** |
| market-sizing-analysis | 2 | 3 | 4 | 4 | 5 | **35** |
| analyzing-financial-statements | 2 | 2 | 3 | 4 | 4 | **28** |
| startup-financial-modeling | 2 | 2 | 4 | 4 | 4 | **30** |
| team-composition-analysis | 2 | 2 | 4 | 3 | 5 | **31** |
| lead-research-assistant | 2 | 2 | 3 | 4 | 4 | **28** |
| competitive-ads-extractor | 2 | 2 | 4 | 4 | 4 | **30** |

### Productivity Skills (15)

| Skill | Freq | Breadth | Gap | Quality | VP | **Total** |
|-------|------|---------|-----|---------|----|----|
| pdf | 3 | 3 | 2 | 3 | 3 | **27** |
| write-concept | 2 | 2 | 2 | 3 | 2 | **20** |
| write-docs | 3 | 3 | 2 | 3 | 3 | **27** |
| fact-check | 3 | 4 | 3 | 3 | 4 | **34** |
| vibe-workflow | 2 | 2 | 3 | 3 | 2 | **22** |
| concept-workflow | 2 | 2 | 3 | 3 | 2 | **22** |
| obsidian-bases | 2 | 2 | 4 | 3 | 2 | **24** |
| notebooklm-skill-master | 2 | 2 | 4 | 3 | 3 | **26** |
| generate-status-report | 4 | 3 | 4 | 4 | 5 | **40** |
| progress-report | 3 | 3 | 3 | 3 | 4 | **31** |
| claude-md-manager | 2 | 2 | 4 | 3 | 2 | **24** |
| openai-knowledge | 2 | 2 | 3 | 3 | 2 | **22** |
| prompt-lookup | 2 | 2 | 3 | 3 | 2 | **22** |
| get-available-resources | 2 | 2 | 3 | 3 | 2 | **22** |
| resource-curator | 2 | 2 | 3 | 3 | 3 | **24** |

### Design Skills (3)

| Skill | Freq | Breadth | Gap | Quality | VP | **Total** |
|-------|------|---------|-----|---------|----|----|
| ui-ux-pro-max | 2 | 3 | 3 | 4 | 3 | **28** |
| ux-researcher-designer | 2 | 2 | 3 | 4 | 3 | **26** |
| scientific-schematics | 2 | 2 | 4 | 3 | 2 | **24** |

---

## Top 25 Skills (Ranked by Score)

| Rank | Skill | Score | Category |
|------|-------|-------|----------|
| 1 | knowledge-verification-protocol | 50 | Core |
| 2 | adam-perry-onboarding | 48 | Core |
| 3 | bpo-goaling | 42 | Business |
| 4 | exploratory-data-analysis | 42 | Data |
| 5 | data-storytelling | 42 | Data |
| 6 | executing-plans | 42 | Business |
| 7 | lorazepam-protocol | 42 | Core |
| 8 | context-saver | 40 | Core |
| 9 | ceo-advisor | 40 | Business |
| 10 | plan-writing | 40 | Business |
| 11 | generate-status-report | 40 | Productivity |
| 12 | knowledge-distillation | 38 | Core |
| 13 | product-manager-toolkit | 38 | Business |
| 14 | python-data-visualization | 37 | Data |
| 15 | scientific-brainstorming | 37 | Core |
| 16 | anti-survivorship-memory | 37 | Core |
| 17 | kpi-dashboard-design | 36 | Data |
| 18 | market-research-reports | 36 | Business |
| 19 | handoff | 35 | Core |
| 20 | mct-handoff | 35 | Core |
| 21 | market-sizing-analysis | 35 | Business |
| 22 | fact-check | 34 | Productivity |
| 23 | systematic-debugging | 33 | Development |
| 24 | agent-builder | 33 | Development |
| 25 | session-memory | 33 | Core |

---

## Summary by Tier

**Essential (40+): 11 skills**
- All Core skills in top 25
- Business dominates this tier

**High Value (30-39): 14 skills**
- Data visualization and storytelling
- Development fundamentals
- Productivity reporting

**Excluded from Top 25 (under 33):**
- Specialized scientific tools (anndata, deeptools, neurokit2)
- Narrow technical skills (model-compression, optimizing-attention-flash)
- Niche integrations (n8n, langsmith)

---

## Recommended Top 25 for Claude Desktop

1. knowledge-verification-protocol
2. adam-perry-onboarding
3. lorazepam-protocol
4. context-saver
5. knowledge-distillation
6. scientific-brainstorming
7. anti-survivorship-memory
8. handoff
9. mct-handoff
10. session-memory
11. bpo-goaling
12. ceo-advisor
13. executing-plans
14. plan-writing
15. product-manager-toolkit
16. market-research-reports
17. market-sizing-analysis
18. exploratory-data-analysis
19. data-storytelling
20. python-data-visualization
21. kpi-dashboard-design
22. generate-status-report
23. fact-check
24. systematic-debugging
25. agent-builder
