# Top 25 Claude Skills - Ready for Upload

**Generated:** 2026-01-27
**Total Files:** 25 (within 50-file Claude Desktop limit)

## Upload Instructions

### Option 1: Claude Desktop Project (Recommended)

1. Open Claude Desktop
2. Create a new Project or use existing
3. Click **"Add content"** → **"Upload files"**
4. Select all 25 `.md` files from this folder
5. Claude will now have access to these skills in that Project

### Option 2: MCP Filesystem Server

Add to your Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "skills": {
      "command": "npx",
      "args": [
        "-y",
        "@anthropic/mcp-server-filesystem",
        "/Users/adam.perry/Library/Mobile Documents/com~apple~CloudDocs/Obsidian/aep.brain.II/Atlas/AI Skills/.export/top-25"
      ]
    }
  }
}
```

## Skill List (Ranked by Score)

| # | Skill | Score | Category |
|---|-------|-------|----------|
| 01 | knowledge-verification-protocol | 50 | Core |
| 02 | adam-perry-onboarding | 48 | Core |
| 03 | bpo-goaling | 42 | Business |
| 04 | exploratory-data-analysis | 42 | Data |
| 05 | data-storytelling | 42 | Data |
| 06 | executing-plans | 42 | Business |
| 07 | lorazepam-protocol | 42 | Core |
| 08 | context-saver | 40 | Core |
| 09 | ceo-advisor | 40 | Business |
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

## Category Distribution

- **Core:** 10 skills (context, verification, memory)
- **Business:** 7 skills (strategy, planning, analysis)
- **Data:** 4 skills (visualization, analysis, storytelling)
- **Productivity:** 2 skills (reports, fact-checking)
- **Development:** 2 skills (debugging, agents)

## Usage

Once uploaded, reference skills naturally in conversation:
- "Use the knowledge-verification-protocol to fact-check this"
- "Apply bpo-goaling framework to these objectives"
- "Help me with exploratory-data-analysis on this CSV"

Claude will automatically apply the relevant skill's methodology.
