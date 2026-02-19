# Skills Inventory

**Last Updated:** February 19, 2026
**Total Skills:** 144 (70 existing + 74 newly installed)
**Repository Version:** 3.0

## Overview

This inventory tracks all Claude Code skills available in the aep-skills repository and organized in the Obsidian vault at `Atlas/AI Skills/`.

## Installation Date Reference

**Initial Commit:** 74 skills installed via `npx skills add` from various GitHub repositories
**Installation Date:** February 19, 2026
**Installation Period:** Single batch installation from multiple sources

## Skills by Category

### Planning & Orchestration (29 skills) - NEW CATEGORY
**Installation Date:** 2026-02-19
**Source Repositories:** Multiple (sickn33, jackspace, mineru98, outfitter-dev, cfircoo, etc.)

**Planning Skills (19):**
- planning
- planning-with-files
- planning-agent
- planning-assistant
- planning-documentation
- planning-under-uncertainty
- planning-validate
- planning-workflow
- agile-sprint-planning
- campaign-planning
- capacity-planning
- concise-planning
- dev-workflow-planning
- feature-planning
- pi-planning-with-files
- release-planning
- strategic-planning
- task-planning
- technical-roadmap-planning

**Subagent Skills (10):**
- subagents
- create-subagents
- codex-subagents
- orchestrate-subagents
- subagents-orchestration-guide
- working-with-subagents
- ring-testing-agents-with-subagents
- ring-testing-skills-with-subagents
- testing-skills-with-subagents
- testing-workflows-with-subagents

### Development (27 skills)
**New Skills Added:** 14

**Obsidian Integration (9):**
- obsidian
- obsidian-bases
- obsidian-canvas
- obsidian-canvas-creator
- obsidian-cli
- obsidian-clipper-template-creator
- obsidian-dashboard
- obsidian-markdown
- obsidian-vault-management

**Development Tools (5):**
- git-workflow
- elevenlabs-agents
- fastapi-customer-support-tech-enablement
- headless-adapters
- explanatory-playground

**Original Skills (13):**
- docstring
- move-code-quality
- systematic-debugging
- sql-optimization-patterns
- dbt-transformation-patterns
- schema-exploration
- query-writing
- n8n-workflow-patterns
- n8n-code-javascript
- d3-viz
- artifacts-builder
- agent-builder
- optimizing-attention-flash

### Data & Analytics (24 skills)
**New Skills Added:** 7

**Evaluation & Testing (7):**
- agent-eval-harness
- eval-harness
- evaluating-llms-harness
- evaluation-harness
- harness-writing
- test-generation
- worldthreatmodelharness

**Original Skills (17):**
- python-data-visualization
- grafana-dashboards
- kpi-dashboard-design
- exploratory-data-analysis
- senior-data-scientist
- statsmodels
- data-storytelling
- geopandas
- networkx
- anndata
- neurokit2
- deeptools
- vector-index-tuning
- tensorboard
- model-compression
- hypogenic
- google-analytics

### Business (22 skills)
**New Skills Added:** 10

**Customer Support & Success (10):**
- customer-support
- customer-support-builder
- customer-support-ai-tools
- customer-success
- customer-success-manager
- customer-journey-map
- customer-review-aggregator
- customer-training-curriculum
- support-systems-architect
- support-ticket-triage

**Original Skills (12):**
- ceo-advisor
- market-research-reports
- market-sizing-analysis
- analyzing-financial-statements
- startup-financial-modeling
- plan-writing
- executing-plans
- product-manager-toolkit
- bpo-goaling
- team-composition-analysis
- competitive-ads-extractor
- lead-research-assistant

### Productivity (25 skills)
**New Skills Added:** 10

**Documentation & Writing (10):**
- doc-brd
- user-guide-creation
- response-drafting
- interactive-writing-assistant
- presentation-builder
- meeting-facilitator
- markdown-slides
- defuddle
- chatwoot
- budget-advisor

**Original Skills (15):**
- pdf
- write-concept
- write-docs
- fact-check
- vibe-workflow
- concept-workflow
- obsidian-bases
- notebooklm-skill-master
- generate-status-report
- progress-report
- claude-md-manager
- openai-knowledge
- prompt-lookup
- get-available-resources
- resource-curator

### Design (7 skills)
**New Skills Added:** 4

**Visualization & Diagramming (4):**
- mermaid-visualizer
- excalidraw-diagram
- json-canvas
- web-scraping

**Original Skills (3):**
- ui-ux-pro-max
- ux-researcher-designer
- scientific-schematics

### Core (10 skills)
**Status:** No new skills added (foundational skills remain unchanged)

- knowledge-verification-protocol
- lorazepam-protocol
- context-saver
- session-memory
- handoff
- mct-handoff
- knowledge-distillation
- scientific-brainstorming
- anti-survivorship-memory
- adam-perry-onboarding

## Source Repositories

Skills were installed from the following GitHub repositories:

- sickn33/antigravity-awesome-skills (848 skills available)
- jackspace/claudeskillz (250 skills available)
- mineru98/skills-store (13 skills available)
- outfitter-dev/agents (56 skills available)
- cfircoo/claude-code-toolkit (15 skills available)
- shinpr/claude-code-workflows (11 skills available)
- arittr/spectacular (14 skills available)
- lerianstudio/ring (80 skills available)
- cpfiffer/central (19 skills available)
- ed3dai/ed3d-plugins (37 skills available)
- shhac/skills (5 skills available)
- kyldvs/setup (8 skills available)
- wln/obra-superpowers (20 skills available)
- lifangda/claude-plugins (200 skills available)
- krosebrook/source-of-truth-monorepo (63 skills available)
- vladm3105/aidoc-flow-framework (80 skills available)
- Many others...

## Installation Notes

- Skills are physically stored in `.agents/skills/` directory
- Skills are symlinked in `.claude/skills/` for Claude Code compatibility
- Skills are organized in Obsidian vault at `Atlas/AI Skills/[Category]/[skill-name]/`
- All skills follow standard markdown with YAML frontmatter structure
- Progressive disclosure system maintained (SKILL-INDEX → Category TOCs → Individual SKILLs)
- Token efficiency preserved through three-tier loading protocol

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.0 | 2026-02-19 | Added 74 new skills, created Planning & Orchestration category, updated all TOCs |
| 2.0 | 2026-02-19 | Initial master/aep-skills command for skills discovery |
| 1.0 | 2026-02-19 | Initial commit with core skills (ddbranding, obsidian, aep-brain-skills) |

## Obsidian Vault Integration

All skills are documented and cross-referenced in the Obsidian vault structure:

```
Atlas/AI Skills/
├── .index/
│   ├── SKILL-INDEX.md (master index)
│   ├── GLOBAL-SKILLS.md
│   └── CLAUDE-INSTRUCTIONS.md
├── .toc/
│   ├── CORE-TOC.md
│   ├── PLANNING-TOC.md
│   ├── DEV-TOC.md
│   ├── DATA-TOC.md
│   ├── BUSINESS-TOC.md
│   ├── PRODUCTIVITY-TOC.md
│   └── DESIGN-TOC.md
└── [Category]/
    ├── [skill-name]/
    │   ├── SKILL.md
    │   ├── references/
    │   ├── templates/
    │   ├── scripts/
    │   └── assets/
    └── .toc/
        └── [CATEGORY]-TOC.md
```

## Maintenance Notes

- Skills requiring updates should have their SKILL.md files modified
- New categories can be added by creating new directories and updating SKILL-INDEX.md
- The progressive disclosure system should always be maintained to preserve token efficiency
- Backlinks in Obsidian should be verified regularly using Obsidian's broken link finder
- Version numbers should be incremented when significant skill sets are added

## Future Enhancements

Potential areas for expansion:
- Additional planning methodologies
- More evaluation/testing frameworks
- Extended Obsidian integrations
- Customer support automation tools
- Additional visualization and diagramming capabilities
