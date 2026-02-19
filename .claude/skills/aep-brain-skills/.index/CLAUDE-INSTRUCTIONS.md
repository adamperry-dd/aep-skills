# Claude Configuration for aep.brain.II

## Skill Loading Protocol

This vault contains 70 skills organized in a hierarchical structure for efficient token usage.

### Layer 1: Always Loaded (at session start)
- **SKILL-INDEX.md** - Master index with category triggers (~500 tokens)
- **GLOBAL-SKILLS.md** - Summary of core skills always available (~400 tokens)

### Layer 2: On-Demand Category TOCs
When user context matches a category, load that category's TOC:
- `Core/.toc/CORE-TOC.md` - 10 skills (context, verification, research, user preferences)
- `Data & Analytics/.toc/DATA-TOC.md` - 17 skills
- `Development/.toc/DEV-TOC.md` - 13 skills
- `Business/.toc/BUSINESS-TOC.md` - 12 skills
- `Productivity/.toc/PRODUCTIVITY-TOC.md` - 15 skills
- `Design/.toc/DESIGN-TOC.md` - 3 skills

### Layer 3: Specific Skills
From the TOC, load only the specific skill needed:
- `[Category]/[skill-name]/SKILL.md`

## How to Use This System

### Step 1: Read the Index
At session start, read `Atlas/AI Skills/.index/SKILL-INDEX.md` to know what's available.

### Step 2: Match User Intent to Category
When user makes a request, identify which category matches:
- "verify this fact" / "is this current" → Core
- "analyze this data" → Data & Analytics
- "help me debug" → Development
- "create a presentation" → Productivity
- "design a dashboard" → Design
- "plan this project" → Business

### Step 3: Load Category TOC
Read the matching category's TOC file to see available skills.

### Step 4: Load Specific Skill
Read only the SKILL.md file for the skill you need.

### Step 5: Execute
Follow the skill's instructions to help the user.

## Token Budget

| Component | Tokens | When Loaded |
|-----------|--------|-------------|
| SKILL-INDEX.md | ~500 | Always |
| GLOBAL-SKILLS.md | ~400 | Always |
| Category TOC | ~200 | On category match |
| Specific skill | Varies | On skill need |
| **Session start** | **~900** | Automatic |

Target: <3,000 tokens at startup (vs. 40,000 loading all skills flat)

## Important Rules

1. **Never load all skills** - Use progressive disclosure
2. **Match before loading** - Only load what user needs
3. **Core skills are foundational** - Load for verification, context, research
4. **Use TOCs as menus** - Don't guess skill names, check the TOC
5. **One skill at a time** - Load, use, then load another if needed

## File Locations

- Index: `Atlas/AI Skills/.index/`
- TOCs: `Atlas/AI Skills/[Category]/.toc/`
- Skills: `Atlas/AI Skills/[Category]/[skill-name]/SKILL.md`

## Categories

| Category | Skills | Purpose |
|----------|--------|---------|
| Core | 10 | Context management, verification, research, user preferences |
| Data & Analytics | 17 | Data analysis, visualization, ML, statistics |
| Development | 13 | Code quality, debugging, SQL, APIs |
| Business | 12 | Strategy, finance, market research, PM, sales |
| Productivity | 15 | Documents, files, content, workflows |
| Design | 3 | UI/UX, wireframes, schematics |

**Total: 70 skills**

---

*Hierarchical loading system v2.0 - Consolidated & optimized*
