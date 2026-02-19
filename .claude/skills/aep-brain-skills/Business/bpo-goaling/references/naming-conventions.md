# Naming Conventions Reference

## Table of Contents
1. [LOB Name Mappings](#lob-name-mappings)
2. [Queue Names](#queue-names)
3. [Partner Standardization](#partner-standardization)
4. [Metric Names](#metric-names)
5. [Merged Channel Logic](#merged-channel-logic)
6. [Goal ID Structure](#goal-id-structure)

---

## LOB Name Mappings

Sigma Goal IDs use different names than Initiative file headers.

| Sigma Goal ID | Initiative File | Notes |
|--------------|----------------|-------|
| Mainline | Mainline | Direct match |
| VIP Queues | VIP | Shortened in Initiative |
| Spanish Queues | Spanish | Shortened in Initiative |
| Cx Specialized Pod | Cx Specialized | Direct match |
| Dx Direct and Payments | DxDirect & PPod | **MERGED CHANNEL** |
| Non-Live/App Troubleshooting | DxNL/TS | **MERGED CHANNEL** |

---

## Queue Names

| Queue | Channel | Customer Type | Notes |
|-------|---------|---------------|-------|
| CxPhone | Phone | Consumer | Mainline |
| CxChat | Chat | Consumer | Mainline |
| DxPhone | Phone | Dasher | Mainline |
| DxChat | Chat | Dasher | Mainline |
| CxPhoneSp | Phone | Consumer | Spanish |
| CxChatSp | Chat | Consumer | Spanish |
| DxPhoneSp | Phone | Dasher | Spanish |
| DxChatSp | Chat | Dasher | Spanish |

---

## Partner Standardization

| Raw Name (may appear in files) | Standardized Name |
|-------------------------------|-------------------|
| TTEC | TTec |
| Telus | TP |
| CP360 | Contact Point 360 |
| Alorica | Alorica |
| TaskUs | TaskUs |
| Concentrix | Concentrix |
| VXI | VXI |
| MZA | MZA |

**Note**: Always verify partner names against the source file—new partners may be added.

---

## Metric Names

| Sigma Goal ID | Initiative File | Data Format |
|--------------|----------------|-------------|
| Contact AHT | AHT | Minutes (decimal: 6.50) |
| TxFCR | FCR | Percentage as decimal (0.950) |
| DWR | DWR | Percentage as decimal (0.820) |

---

## Merged Channel Logic

### Critical Rule

For certain LOBs, the Initiative file has **ONE set of combined Chat+Phone values** that must be used for **BOTH** DxChat and DxPhone Goal IDs.

### Merged LOBs

#### 1. DxDirect & PPod (Dx Direct and Payments)

**Initiative file row label:** "DxDirect & PPod AHT (Chat & Phone)"

**Creates entries for:**
- `Dx Direct and Payments-DxChat-{Partner}`
- `Dx Direct and Payments-DxPhone-{Partner}`

Both use the same weekly values from the single Initiative row.

#### 2. DxNL/TS Pod (Non-Live/App Troubleshooting)

**Initiative file row label:** "DxNL/TS AHT (Chat & Phone)"

**Creates entries for:**
- `Non-Live/App Troubleshooting-DxChat-{Partner}`
- `Non-Live/App Troubleshooting-DxPhone-{Partner}`

Both use the same weekly values from the single Initiative row.

### Implementation Pattern

```python
MERGED_LOBS = {
    'Dx Direct and Payments': ['DxChat', 'DxPhone'],
    'Non-Live/App Troubleshooting': ['DxChat', 'DxPhone']
}

# When extracting from Initiative file:
if lob in MERGED_LOBS:
    for queue_type in MERGED_LOBS[lob]:
        # Create entry for EACH queue type using SAME values
        create_goal_entry(lob, queue_type, partner, values)
```

---

## Goal ID Structure

### Format

```
BPO-{Quarter}-{Year}-Weekly-Team-{Metric}---_{LOB}-{Queue}-{Partner}
```

### Components

| Component | Values | Examples |
|-----------|--------|----------|
| Quarter | Q1, Q2 | Q1 |
| Year | 4-digit | 2026 |
| Metric | DWR, TxFCR, Contact AHT | DWR |
| LOB | See LOB mappings | Mainline, Dx Direct and Payments |
| Queue | See Queue names | DxChat, CxPhone |
| Partner | See Partner names | Alorica, TaskUs |

### Examples

```
BPO-Q1-2026-Weekly-Team-DWR---_Mainline-DxChat-Alorica
BPO-Q2-2026-Weekly-Team-Contact AHT---_Dx Direct and Payments-DxChat-TaskUs
BPO-Q1-2026-Weekly-Team-TxFCR---_Spanish Queues-CxPhoneSp-TTec
```

### Parsing Gotchas

**Problem**: LOBs can contain hyphens and slashes:
- "Dx Direct and Payments"
- "Non-Live/App Troubleshooting"

**Solution**: Always parse from RIGHT using rsplit:

```python
# Split on '---_' first (reliable separator)
prefix, suffix = goal_id.split('---_')

# Parse suffix from RIGHT to get partner (single token)
lob_queue, partner = suffix.rsplit('-', 1)

# Then split LOB from queue
# Queue is always last component before partner
```

### Special Case: "Non-Live/App Troubleshooting"

**CRITICAL:** This LOB contains a forward slash ("/").

**Example Goal ID:**
```
BPO-Q1-2026-Weekly-Team-Contact AHT---_Non-Live/App Troubleshooting-DxChat-TaskUs
```

**Parsing Steps:**
1. Split on `---_` → `suffix = "Non-Live/App Troubleshooting-DxChat-TaskUs"`
2. RSPLIT on `-` from right → `lob_queue = "Non-Live/App Troubleshooting-DxChat"`, `partner = "TaskUs"`
3. Handle special case:
   ```python
   if lob_queue.startswith('Non-Live'):
       lob = 'Non-Live/App Troubleshooting'
       queue = lob_queue.replace('Non-Live/App Troubleshooting-', '')
   else:
       lob, queue = lob_queue.split('-', 1)
   ```

**Why This Matters:**
- H1 2026 incident: 19 goals marked "unknown source" due to incorrect parsing
- Naive split on "/" breaks the LOB name: "Non" vs "Live/App Troubleshooting"
- Must treat "Non-Live/App Troubleshooting" as atomic string

See `scripts/parse_goal_id.py` for robust implementation.
