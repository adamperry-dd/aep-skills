---
name: global-skills
description: Core skills overview - essential context management, verification, and research capabilities. Use when needing fact-checking, session continuity, or research methodology guidance.
always_load: true
---

# Core Skills Overview (10 skills)

These skills are foundational for every session. Full details in `Core/.toc/CORE-TOC.md`.

## Knowledge & Verification

| Skill | Purpose | Triggers |
|-------|---------|----------|
| knowledge-verification-protocol | Distinguish stable vs time-sensitive facts, handle temporal truth | verify, fact-check, is this current, latest version |
| lorazepam-protocol | Prevent circular reasoning in audits | audit, validate, compare, "you're spiraling" |

## Context Management

| Skill | Purpose | Triggers |
|-------|---------|----------|
| context-saver | Preserve important conversation context | save context, remember this |
| session-memory | Track session state and decisions | what did we decide, earlier |
| handoff | Transfer context between sessions | handoff, context transfer |
| mct-handoff | Healthy skepticism and cognitive bias prevention | jumping to conclusions, overconfidence, confirmation bias |

## Research & Synthesis

| Skill | Purpose | Triggers |
|-------|---------|----------|
| knowledge-distillation | Summarize complex information | summarize, distill, TL;DR |
| scientific-brainstorming | Research ideation methodology | brainstorm, hypotheses, methodology |
| anti-survivorship-memory | Reduce selection bias and memory limits | survivorship bias, recommendations from examples, RAG memory |

## User Context

| Skill | Purpose | Triggers |
|-------|---------|----------|
| adam-perry-onboarding | User persona, VP-grade output, truth hygiene | Adam Perry, collaboration preferences |

---

## Loading Additional Skills

When user context matches a domain, load from SKILL-INDEX.md:
1. Check which category matches user intent
2. Load that category's TOC
3. Load only the specific skill needed

**Categories:** Core (10), Data & Analytics (17), Development (13), Business (12), Productivity (15), Design (3)

**Never load all skills at once.**
