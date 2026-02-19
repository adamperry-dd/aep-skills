---
name: skill-index
description: Master index of all available skills organized by category. Load this at session start to enable on-demand skill discovery. When user context matches a category, load that category's TOC for detailed skill selection.
always_load: true
---

# Skill Index

## How to Use
1. This index loads automatically at session start
2. When user mentions concepts from a category, load that category's TOC
3. From the TOC, load only the specific skill needed
4. Never load all skills at once - use progressive disclosure

## Categories

### 📊 Data & Analytics (17 skills)
**Load when:** data analysis, visualization, charts, graphs, statistics, machine learning, scientific computing, pandas, matplotlib, plotly, seaborn
**TOC:** @Data & Analytics/.toc/DATA-TOC.md

### 💻 Development (13 skills)
**Load when:** code quality, debugging, SQL, database, dbt, n8n workflows, API development, artifacts, D3 visualization
**TOC:** @Development/.toc/DEV-TOC.md

### 💼 Business (12 skills)
**Load when:** strategy, financial analysis, market research, project planning, BPO goals, executive presentations, startup modeling, lead research, competitive ads
**TOC:** @Business/.toc/BUSINESS-TOC.md

### 📝 Productivity (15 skills)
**Load when:** documents, files, Excel, PDF, PowerPoint, content writing, Obsidian, status reports, workflows, templates
**TOC:** @Productivity/.toc/PRODUCTIVITY-TOC.md

### 🎨 Design (3 skills)
**Load when:** UI/UX design, user interface, visual design, wireframes, prototypes, scientific diagrams, schematics
**TOC:** @Design/.toc/DESIGN-TOC.md

### 🔧 Core (10 skills) - ALWAYS AVAILABLE
**Load when:** fact-checking, context management, session handoff, knowledge verification, audit validation, research methodology, user preferences, survivorship bias
**TOC:** @Core/.toc/CORE-TOC.md
**Key skills:**
- knowledge-verification-protocol: Verify facts, temporal truth, determine if web search needed
- lorazepam-protocol: Prevent circular reasoning in audits
- context-saver, session-memory, handoff: Context management
- scientific-brainstorming, knowledge-distillation: Research & synthesis
- adam-perry-onboarding: User persona and collaboration preferences
- mct-handoff: Metacognitive training for healthy skepticism
- anti-survivorship-memory: Reduce selection bias and memory limits

---
*Index version 2.0 | Skills across 6 categories: Core (10), Data (17), Dev (13), Business (12), Productivity (15), Design (3) | Total: 70*
