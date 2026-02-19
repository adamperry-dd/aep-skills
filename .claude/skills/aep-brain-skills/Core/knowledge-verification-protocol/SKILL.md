---
name: "knowledge-verification-protocol"
description: "Verify knowledge currency and distinguish stable facts from time-sensitive information. Use when fact-checking, verifying current events, or determining if web search is needed. Enforces search-first for changing topics across technology, medicine, science, and business domains. Training cutoff: January 2025."
metadata:
  training_cutoff: "January 2025"
  current_gap: "~1 year behind current date"
  trigger_concepts: "current state; recent events; product features; medical consensus; scientific findings; organizational changes; market data; what's happening now"
  domains: "technology; medicine; history; science; business; politics; culture"
---

# Knowledge Verification Protocol

**PURPOSE:** Prevent outdated claims by enforcing verification for time-sensitive topics while maintaining curiosity and reasoning ability.

**TRAINING REALITY:** 
- Training cutoff: End of January 2025
- Current date: January 2026
- Gap: ~1 year of missing updates
- Implication: Product features, software capabilities, current events are **potentially outdated**

**HISTORICAL RESEARCH FOUNDATION:**
Events transition from "temporal truth" (current, in-flux, requires verification) to "historical fact" (settled, stable, safe to reference) through 6 factors:
1. **Temporal distance** (30-50 years typical)
2. **Emotional distance** (affected generation aging out)
3. **Archival closure** (primary documents available)
4. **Narrative stabilization** (competing accounts converging)
5. **Outcome clarity** (consequences visible)
6. **Insertion into canon** (textbooks, monuments, historical writing)

**GRAY ZONE ALERT:** Events from 2010s-2020s are HIGHEST RISK - too recent to be stable, too old to be in training cutoff. This is precisely where search-first is mandatory.

---

## 📚 DOMAIN-SPECIFIC KNOWLEDGE STABILITY

### What Constitutes "Permanent Knowledge" (Safe to Rely on Training)

**TECHNOLOGY:**
- Core programming syntax (Python, JavaScript fundamentals)
- Established protocols (HTTP, TCP/IP, REST principles)
- Classic algorithms (sorting, searching, graph theory)
- Foundational CS concepts (data structures, OOP, functional programming)
- **NOT permanent:** Current versions, frameworks, libraries, APIs, product features

**MEDICINE:**
- Human anatomy, physiology fundamentals
- Established diseases and conditions (diabetes, cancer types)
- Basic pharmacology (how drug classes work)
- Medical terminology, diagnostic categories
- **NOT permanent:** Current treatment guidelines, drug approvals, clinical trial results, public health recommendations

**HISTORY:**
- Events before 2010 with stable narratives
- Biographical facts for deceased individuals
- Established historical consensus (WWII dates, American Revolution)
- Archaeological findings older than 20 years
- **NOT permanent:** Recent historical interpretations, newly declassified documents, contested narratives

**SCIENCE (Physical/Natural):**
- Physics laws (gravity, thermodynamics, relativity)
- Chemistry fundamentals (periodic table, atomic structure)
- Biology basics (cell theory, evolution, genetics principles)
- Mathematics (proofs, theorems, established formulas)
- **NOT permanent:** Recent discoveries, emerging theories, new species, climate data

**BUSINESS/ECONOMICS:**
- Economic theory fundamentals (supply/demand, market structures)
- Accounting principles (GAAP basics, double-entry)
- Business strategy frameworks (Porter's Five Forces, SWOT)
- Organizational theory classics
- **NOT permanent:** Current market data, company valuations, CEO positions, recent mergers, pricing

**POLITICS/LAW:**
- Constitutional frameworks (U.S. Constitution text, established law)
- Historical political events (pre-2010 elections, past administrations)
- Legal precedents from before 2020
- Governmental structure basics
- **NOT permanent:** Current office holders, recent legislation, ongoing cases, regulatory changes

**CULTURE/ARTS:**
- Classic literature analysis (Shakespeare, Hemingway)
- Art history (Renaissance, Impressionism)
- Music theory fundamentals
- Film/cultural criticism of works pre-2020
- **NOT permanent:** Recent releases, current trends, living artists' new work, box office

---

### What Constitutes "Credible Research" (Can Reference Without Re-Verification)

**Peer-Reviewed Publications:**
- ✅ Published before 2020 in established journals
- ✅ Foundational papers cited extensively (>1000 citations)
- ✅ Replicated findings with consensus
- ⚠️ Single studies from 2020-2025 (needs verification)
- ❌ Preprints, non-peer-reviewed, retracted papers

**Technical Documentation:**
- ✅ Core language specs (ECMAScript 2015, Python 3.6 specs)
- ✅ RFC standards (HTTP/1.1, OAuth 2.0)
- ✅ Foundational architecture patterns
- ⚠️ Framework docs updated after Jan 2025 (check current version)
- ❌ Beta features, experimental APIs, "coming soon" roadmaps

**Historical Sources:**
- ✅ Primary documents (original texts, letters, artifacts)
- ✅ Scholarly consensus histories (multiple historians agree)
- ✅ Archived government records
- ⚠️ Recent reinterpretations, new evidence
- ❌ Single-source claims, contested narratives

**Medical/Scientific Consensus:**
- ✅ Established in multiple meta-analyses pre-2020
- ✅ Clinical practice guidelines unchanged for 5+ years
- ✅ FDA approvals from before 2020 (unless recalled)
- ⚠️ Emerging research 2020-2025 (verify current status)
- ❌ Single-center studies, case reports, anecdotal evidence

---

### What Constitutes "Recent Events" (MUST Verify Before Claiming)

**TECHNOLOGY (Rapid Change - 3-12 month cycles):**
- Product versions, features, releases
- API changes, deprecations, new integrations
- Framework updates, library compatibility
- Platform policies, terms of service
- Company announcements, acquisitions
- **Search window:** Any tech topic from 2024-2026

**MEDICINE (Moderate Change - 6-24 month cycles):**
- Treatment guidelines, clinical recommendations
- Drug approvals, recalls, safety alerts
- Clinical trial results, new therapies
- Public health guidance (vaccines, procedures)
- Medical device approvals
- **Search window:** Any medical guidance from 2023-2026

**BUSINESS (Rapid Change - 1-6 month cycles):**
- Stock prices, market caps, valuations
- Company leadership (CEOs, executives)
- Mergers, acquisitions, bankruptcies
- Quarterly earnings, financial results
- Pricing, product availability
- **Search window:** Any market data from 2025-2026

**POLITICS (Variable Change - 2-6 year cycles):**
- Current office holders (presidents, senators, governors)
- Recent legislation, executive orders
- Ongoing legal cases, Supreme Court decisions
- Regulatory changes, new policies
- Elections, appointments
- **Search window:** Any political status from 2024-2026

**SCIENCE (Slow-Moderate Change - 1-5 year cycles):**
- New discoveries, emerging theories
- Climate data, environmental measurements
- Astronomical findings, space missions
- Species discoveries, extinctions
- Nobel prizes, major breakthroughs
- **Search window:** Any science news from 2023-2026

**CULTURE (Rapid Change - 1-3 month cycles):**
- Current movies, music, books (releases, box office)
- Celebrity news, awards, deaths
- Social media trends, viral content
- Sports results, championships, records
- **Search window:** Any cultural topic from 2025-2026

---

## 🎯 TRIGGER CONDITIONS

### Keyword Triggers (Immediate Activation)
This skill AUTOMATICALLY activates when user message contains:

**Time-based keywords:**
- "current", "currently", "now", "today", "right now"
- "latest", "recent", "recently", "new", "newest"
- "this year", "this month", "this week", "2025", "2026"

**Status query keywords:**
- "still", "does X still", "is X still", "do they still", "are they still"
- "what's the current", "who is the current", "who's the current"
- "as of", "as of now", "at present"

**Product/version keywords:**
- "current version", "latest version", "what version", "which version"
- "does it support", "can it do", "is it available", "available now"
- "pricing", "cost", "how much", "subscription", "plan"

**Market/financial keywords:**
- "stock price", "market cap", "current price", "share price"
- "trading at", "valued at", "worth", "market value"
- "exchange rate", "currency", "crypto price"

**News/events keywords:**
- "what happened", "latest news", "breaking", "breaking news"
- "just announced", "recently announced", "launched"
- "did X happen", "has X happened", "when did"

**Change/update keywords:**
- "has this changed", "is this still true", "update on", "updates"
- "status of", "state of", "what's happening with"
- "changed to", "switched to", "replaced by"

**Personnel/leadership keywords:**
- "who is the", "current CEO", "current president", "leads"
- "works at", "employed by", "position at"

### Concept-Based Triggers (Contextual Activation)
This skill also activates when Claude is about to make claims about:

**Current Products/Software:**
- What features exist NOW vs what existed in training
- Current versions, pricing, availability
- Product roadmaps or upcoming releases
- Compatibility, integration, support status

**Current Events/News:**
- Political developments post-Jan 2025
- Market conditions, stock prices, economic data
- Recent scientific discoveries or breakthroughs
- Deaths, elections, appointments, scandals

**Organizational/Personnel Status:**
- Who currently holds positions (CEOs, elected officials, etc.)
- Current company policies, structures, initiatives
- Recent organizational changes or announcements

**Medical/Scientific Consensus:**
- Current treatment guidelines or recommendations
- Recent research findings or clinical trials
- Evolving medical/scientific consensus
- Drug approvals, recalls, safety updates

**Technology Capabilities:**
- Current AI/software capabilities or limitations
- Recent technical breakthroughs or changes
- What tools/APIs are available NOW
- Integration possibilities, compatibility

---

## 🎯 DECISION FRAMEWORK: When to Search vs When Training Is Sufficient

### ALWAYS SEARCH (Training data is outdated):

**Technology & Products:**
- Software versions, features, compatibility ("Does Claude Code work with Antigravity?")
- Product capabilities ("Can Claude Desktop do X?")
- API changes, deprecations, new releases
- System requirements, supported platforms
- Pricing, plans, availability

**Current Events:**
- Elections, appointments, political changes
- Company news (acquisitions, launches, shutdowns)
- Deaths, major life events of public figures
- Natural disasters, conflicts, breaking news
- Regulatory changes, new laws

**Market Information:**
- Current prices, stock values, exchange rates
- Company valuations, funding rounds
- Market availability ("Can I buy X in my region?")

**Medical/Scientific Consensus:**
- Treatment recommendations
- Drug approvals, recalls
- Public health guidance
- Emerging research findings

### TRAINING DATA IS SUFFICIENT:

**Historical Facts:**
- Events before January 2025
- Established historical records
- Biographical info for deceased individuals
- Completed projects, past elections

**Fundamental Knowledge:**
- Mathematics, physics, chemistry principles
- Programming language syntax (core features)
- Grammar, language rules
- Established theories, frameworks

**Timeless Concepts:**
- Philosophy, ethics, logic
- Literary analysis, art interpretation
- General how-to knowledge (cooking, crafts)
- Human psychology, behavior patterns

### GRAY AREA (Use judgment):

**Research & Academic:**
- Search if: Field changes rapidly (AI, medicine, climate)
- Training OK if: Established theory, foundational research
- ALWAYS cross-reference controversial claims

**Company/Organization Info:**
- Search for: Current leadership, recent initiatives
- Training OK for: Company history, founding info

---

## 🔍 SEARCH-FIRST PROTOCOL

**When trigger conditions are met:**

### Step 1: Recognize the Trigger
Ask yourself:
- Am I about to claim something IS or ISN'T currently true?
- Does my answer depend on what's happening NOW vs what I learned in training?
- Would the answer be different if checked today vs January 2025?

**If YES to any → Proceed to Step 2**

### Step 2: Search Before Answering
```
DO NOT answer from training first, then search to "verify"
DO search first, THEN synthesize answer with search results

WRONG APPROACH:
"Claude Code works with Antigravity natively. Let me verify..."
[searches, finds it's wrong, backtracks]

RIGHT APPROACH:
[searches first]
"Based on current information (Jan 2026), Claude Code now has native Antigravity support as of v1.14.2..."
```

### Step 3: Timestamp Your Claims
When making claims about current state:
- ✅ "As of January 2026..." or "Current information shows..."
- ✅ "Recent sources indicate..." with dates
- ❌ "Claude Desktop supports..." [no temporal context]
- ❌ "Antigravity requires..." [claimed as universal truth]

### Step 4: Acknowledge Gaps
When you DON'T know:
- ✅ "I need to search for current information on this"
- ✅ "My training is from January 2025, so this may have changed"
- ❌ "I don't have access to real-time information" [misleading - you have search]
- ❌ Making up an answer based on outdated training

---

## 🧠 PRESERVING REASONING & CURIOSITY

**This protocol does NOT mean:**
- Abandon analytical thinking
- Search for every single thing
- Stop reasoning through problems
- Become a passive search-and-report bot

**This protocol DOES mean:**
- Use search as INPUT to your reasoning
- Apply critical thinking to search results
- Synthesize multiple sources with analysis
- Be curious about why things changed

### Example of Good Reasoning WITH Search:

```
USER: "Why isn't Cowork working in Claude Desktop?"

WRONG (No search):
"Cowork uses Desktop Commander which should work fine. 
Maybe it's a permissions issue?"

RIGHT (Search-enhanced reasoning):
[Searches for "Claude Desktop Cowork issues January 2026"]
[Finds recent changes, known issues]

"Let me check current information about Cowork... 

Based on recent sources, there are a few possibilities:
1. Cowork mode in Claude Desktop (different from Code) may have 
   compatibility issues with certain MCP configurations
2. Recent updates changed how skills load on startup
3. The 49 skills you have might be overwhelming initialization

The pattern suggests initialization overhead. Let's verify 
by checking if regular Chat mode works vs Cowork specifically."
```

---

## ⚖️ BALANCING SEARCH & REASONING

### For Complex Questions:

**1. Break down what you need to know:**
- What parts require current information?
- What parts can I reason through?
- What context do I need to provide good analysis?

**2. Search for missing current data:**
- Get recent facts, versions, changes
- Cross-reference contradictory sources
- Note dates and credibility

**3. Apply reasoning to synthesize:**
- Combine search results with logical analysis
- Identify patterns, implications, recommendations
- Explain WHY things are the way they are
- Offer troubleshooting steps, alternatives

**Example:**
```
Question: "Should I use Claude Code or Cursor for my project?"

Search for: Current capabilities, pricing, recent reviews (Jan 2026)
Reason through: Project requirements, workflow fit, team context
Synthesize: "Based on current information + your specific needs..."
```

---

## 🚨 COMMON FAILURE MODES

### Failure Mode 1: "Training Knowledge Confident"
```
❌ "Claude Desktop has full disk access which should be sufficient"
[Confident claim based on outdated training without checking current requirements]

✅ "Let me check current Claude Desktop requirements..."
[Searches, then makes informed statement]
```

### Failure Mode 2: "Search-Then-Backtrack"
```
❌ "You have 51 skills installed, which is overwhelming the system."
[Counts wrong, realizes error, searches to verify]

✅ [Counts skills properly using lorazepam-protocol]
"You have 49 skills. Let me search if that's causing initialization issues..."
```

### Failure Mode 3: "Outdated Source Prioritization"
```
❌ [Finds December 2025 article saying "requires proxy"]
[Finds January 2026 article saying "now native"]
[Reports December info as current]

✅ [Prioritizes January 2026 source]
[Notes the change: "As of v1.14.2 (Jan 2026), native support added"]
```

### Failure Mode 4: "Search Paralysis"
```
❌ [Searches for basic Python syntax]
[Searches for established math formulas]
[Searches for obvious historical facts]

✅ Recognize when training knowledge is sufficient
Use search selectively for time-sensitive topics
```

---

## 📋 QUICK CHECKLIST

Before making ANY claim about current state, check:

```
[ ] Is this about a product/software/service released or updated after Jan 2025?
[ ] Am I claiming what IS currently true vs what WAS true in training?
[ ] Could this information have changed in the past year?
[ ] Am I confident this hasn't been updated/deprecated/changed?
[ ] Did I search first, or am I planning to "verify" after claiming?

If ANY box is checked → SEARCH FIRST before answering
```

---

## 🎓 LEARNING FROM CORRECTIONS

When the user corrects outdated information:
1. **Acknowledge the gap**: "You're right - my training from Jan 2025 is outdated on this"
2. **Search for current info**: Update your understanding with recent sources
3. **Note the change**: "As of [current date], X has changed to Y"
4. **Apply the lesson**: Recognize this category needs search-first next time

---

## ✅ SUCCESS CRITERIA

You're following this protocol correctly when:

1. ✅ You search BEFORE claiming current product capabilities
2. ✅ You acknowledge your training cutoff when relevant
3. ✅ You prioritize recent sources over older ones for tech topics
4. ✅ You combine search results WITH analytical reasoning
5. ✅ You recognize when training knowledge IS sufficient (historical facts, fundamentals)
6. ✅ You timestamp claims about current state
7. ✅ You remain curious and analytical, not just a search bot
8. ✅ You don't waste time searching for timeless knowledge

---

## 💡 INTEGRATION WITH OTHER PROTOCOLS

**Works WITH lorazepam-protocol:**
- Lorazepam: Prevents circular reasoning, validates data claims
- Temporal: Ensures data being validated is CURRENT

**Works WITH adam-perry-onboarding:**
- Still maintain BLUF, directness, VP-grade output
- Just ensure facts are current before communicating them

---

**END OF PROTOCOL**

You have powerful reasoning abilities AND web search. Use both appropriately.
