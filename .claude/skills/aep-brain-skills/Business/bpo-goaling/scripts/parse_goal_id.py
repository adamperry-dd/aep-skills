#!/usr/bin/env python3
"""
Parse BPO Goal IDs into components.

Goal ID Format:
    BPO-{Quarter}-{Year}-Weekly-Team-{Metric}---_{LOB}-{Queue}-{Partner}

Examples:
    BPO-Q1-2026-Weekly-Team-DWR---_Mainline-DxChat-Alorica
    BPO-Q2-2026-Weekly-Team-Contact AHT---_Dx Direct and Payments-DxChat-TaskUs

Usage:
    python parse_goal_id.py "BPO-Q1-2026-Weekly-Team-DWR---_Mainline-DxChat-Alorica"
    python parse_goal_id.py --file goals.csv --column "Unique Goal ID"
"""

import argparse
import json
import sys
from typing import Optional
from dataclasses import dataclass, asdict


@dataclass
class ParsedGoalID:
    quarter: str          # Q1, Q2
    year: str             # 2026
    metric: str           # DWR, FCR, AHT
    metric_raw: str       # DWR, TxFCR, Contact AHT (as in Goal ID)
    lob: str              # Mainline, Dx Direct and Payments, etc.
    queue: str            # DxChat, CxPhone, etc.
    partner: str          # Alorica, TaskUs, etc.
    is_merged_channel: bool  # True if LOB uses merged Chat/Phone values


# LOBs where Initiative file has combined Chat+Phone values
MERGED_CHANNEL_LOBS = {
    'Dx Direct and Payments',
    'Non-Live/App Troubleshooting'
}


def parse_goal_id(goal_id: str) -> Optional[ParsedGoalID]:
    """
    Parse a Goal ID string into components.
    
    Returns None if parsing fails.
    """
    if not goal_id or not isinstance(goal_id, str):
        return None
    
    # Step 1: Split on '---_' (reliable separator between prefix and suffix)
    if '---_' not in goal_id:
        return None
    
    parts = goal_id.split('---_')
    if len(parts) != 2:
        return None
    
    prefix, suffix = parts
    
    # Step 2: Parse prefix for quarter, year, metric
    # Format: BPO-{Quarter}-{Year}-Weekly-Team-{Metric}
    
    # Extract quarter
    if '-Q1-' in prefix:
        quarter = 'Q1'
    elif '-Q2-' in prefix:
        quarter = 'Q2'
    else:
        return None
    
    # Extract year (4 digits after quarter)
    try:
        q_idx = prefix.index(f'-{quarter}-')
        year_start = q_idx + len(f'-{quarter}-')
        year = prefix[year_start:year_start + 4]
        if not year.isdigit():
            return None
    except (ValueError, IndexError):
        return None
    
    # Extract metric (after "Weekly-Team-")
    metric_marker = 'Weekly-Team-'
    if metric_marker not in prefix:
        return None
    
    metric_raw = prefix.split(metric_marker)[1]
    
    # Normalize metric name
    if metric_raw == 'Contact AHT':
        metric = 'AHT'
    elif metric_raw == 'TxFCR':
        metric = 'FCR'
    elif metric_raw == 'DWR':
        metric = 'DWR'
    else:
        metric = metric_raw  # Unknown metric, keep as-is
    
    # Step 3: Parse suffix for LOB, Queue, Partner
    # Format: {LOB}-{Queue}-{Partner}
    # CRITICAL: LOBs can have hyphens, so parse from RIGHT
    
    # Partner is always the last token (no hyphens in partner names)
    suffix_parts = suffix.rsplit('-', 1)
    if len(suffix_parts) != 2:
        return None
    
    lob_queue, partner = suffix_parts
    
    # Now split LOB from Queue
    # Queue names: CxChat, CxPhone, DxChat, DxPhone, CxChatSp, CxPhoneSp, DxChatSp, DxPhoneSp
    known_queues = [
        'CxChat', 'CxPhone', 'DxChat', 'DxPhone',
        'CxChatSp', 'CxPhoneSp', 'DxChatSp', 'DxPhoneSp'
    ]
    
    queue = None
    lob = None
    
    for q in known_queues:
        if lob_queue.endswith(f'-{q}'):
            queue = q
            lob = lob_queue[:-len(f'-{q}')]
            break
    
    if queue is None or lob is None:
        # Fallback: try splitting from right
        lob_queue_parts = lob_queue.rsplit('-', 1)
        if len(lob_queue_parts) == 2:
            lob, queue = lob_queue_parts
        else:
            return None
    
    # Determine if merged channel
    is_merged = lob in MERGED_CHANNEL_LOBS
    
    return ParsedGoalID(
        quarter=quarter,
        year=year,
        metric=metric,
        metric_raw=metric_raw,
        lob=lob,
        queue=queue,
        partner=partner,
        is_merged_channel=is_merged
    )


def main():
    parser = argparse.ArgumentParser(description='Parse BPO Goal IDs')
    parser.add_argument('goal_id', nargs='?', help='Single Goal ID to parse')
    parser.add_argument('--file', '-f', help='CSV file with Goal IDs')
    parser.add_argument('--column', '-c', default='Unique Goal ID', 
                        help='Column name containing Goal IDs')
    parser.add_argument('--json', '-j', action='store_true', 
                        help='Output as JSON')
    
    args = parser.parse_args()
    
    if args.goal_id:
        # Parse single Goal ID
        result = parse_goal_id(args.goal_id)
        if result:
            if args.json:
                print(json.dumps(asdict(result), indent=2))
            else:
                print(f"Quarter: {result.quarter}")
                print(f"Year: {result.year}")
                print(f"Metric: {result.metric} (raw: {result.metric_raw})")
                print(f"LOB: {result.lob}")
                print(f"Queue: {result.queue}")
                print(f"Partner: {result.partner}")
                print(f"Merged Channel: {result.is_merged_channel}")
        else:
            print(f"ERROR: Failed to parse Goal ID: {args.goal_id}", file=sys.stderr)
            sys.exit(1)
    
    elif args.file:
        # Parse Goal IDs from CSV file
        import csv
        
        results = []
        errors = []
        
        with open(args.file, 'r') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, 1):
                goal_id = row.get(args.column, '').strip()
                if goal_id:
                    result = parse_goal_id(goal_id)
                    if result:
                        results.append(asdict(result))
                    else:
                        errors.append({'row': i, 'goal_id': goal_id})
        
        if args.json:
            print(json.dumps({'parsed': results, 'errors': errors}, indent=2))
        else:
            print(f"Parsed: {len(results)} Goal IDs")
            print(f"Errors: {len(errors)} Goal IDs")
            if errors:
                print("\nFailed to parse:")
                for e in errors[:10]:
                    print(f"  Row {e['row']}: {e['goal_id']}")
                if len(errors) > 10:
                    print(f"  ... and {len(errors) - 10} more")
    
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
