---
name: core-toc
description: Table of contents for Core/Global skills - essential protocols always available for context management, verification, and session continuity.
---

# Core Skills (10 skills)

Essential protocols for every session. These skills handle context management, knowledge verification, session continuity, and user-specific preferences.

## Context & Memory

| Skill | Description | Load |
|-------|-------------|------|
| context-saver | Save exploration findings and context to persistent storage. Use when making important discoveries or preserving state. | @context-saver/SKILL.md |
| session-memory | Manages cross-session learning and memory persistence. Use when user asks about previous sessions. | @session-memory/SKILL.md |
| handoff | Hand off to a fresh Claude session. Use when context is full or finishing logical work chunks. | @handoff/SKILL.md |
| mct-handoff | Metacognitive Training for healthy skepticism. Use when exhibiting jumping-to-conclusions, overconfidence, or confirmation bias. | @mct-handoff/SKILL.md |

## User Context

| Skill | Description | Load |
|-------|-------------|------|
| adam-perry-onboarding | Adam Perry's persona and collaboration preferences. Use when interacting with Adam to ensure VP-grade output quality and truth hygiene. | @adam-perry-onboarding/SKILL.md |

## Knowledge Verification

| Skill | Description | Load |
|-------|-------------|------|
| knowledge-verification-protocol | Verify knowledge currency, distinguish stable vs time-sensitive facts, handle temporal truth. Use when fact-checking, checking product features/versions, or determining if web search is needed. | @knowledge-verification-protocol/SKILL.md |

## Reasoning & Research

| Skill | Description | Load |
|-------|-------------|------|
| scientific-brainstorming | Research ideation partner. Use when generating hypotheses, exploring interdisciplinary connections, or developing methodologies. | @scientific-brainstorming/SKILL.md |
| knowledge-distillation | Compress and transfer knowledge using distillation techniques. Use when summarizing complex information or creating smaller models. | @knowledge-distillation/SKILL.md |
| lorazepam-protocol | Prevent circular reasoning and infinite validation loops. Use when auditing data, comparing files, or when user says "you're spiraling". | @lorazepam-protocol/SKILL.md |
| anti-survivorship-memory | Reduce survivorship/selection bias and mitigate memory limits. Use when making recommendations from examples, analyzing metrics with underreported failures, or building RAG/vector memory systems. | @anti-survivorship-memory/SKILL.md |

---
*Core skills provide foundational capabilities for all sessions*
