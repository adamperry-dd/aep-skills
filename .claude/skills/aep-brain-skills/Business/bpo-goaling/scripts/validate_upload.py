#!/usr/bin/env python3
"""
Validate Sigma upload CSV before submission.

Checks:
1. Required columns present
2. Goal ID format valid
3. Date format valid (YYYY-MM-DD, Mondays only)
4. Value format valid (3 decimal places for %, 2 for AHT)
5. No duplicate (Goal ID + Date) combinations
6. Week count per Goal ID (expect 13 per quarter)
7. Walk direction (DWR/FCR up, AHT down)

Usage:
    python validate_upload.py upload.csv
    python validate_upload.py upload.csv --existing sigma_export.csv
    python validate_upload.py upload.csv --json
"""

import argparse
import csv
import json
import sys
from datetime import datetime
from collections import defaultdict
from typing import List, Dict, Set, Tuple

# Import parse_goal_id if available in same directory
try:
    from parse_goal_id import parse_goal_id
except ImportError:
    # Inline minimal parser for standalone use
    def parse_goal_id(goal_id):
        if '---_' not in goal_id:
            return None
        parts = goal_id.split('---_')
        if len(parts) != 2:
            return None
        prefix, suffix = parts
        
        quarter = 'Q1' if '-Q1-' in prefix else ('Q2' if '-Q2-' in prefix else None)
        if not quarter:
            return None
        
        if 'Contact AHT' in prefix:
            metric = 'AHT'
        elif 'TxFCR' in prefix:
            metric = 'FCR'
        elif 'DWR' in prefix:
            metric = 'DWR'
        else:
            metric = 'UNKNOWN'
        
        class Result:
            pass
        r = Result()
        r.quarter = quarter
        r.metric = metric
        return r


REQUIRED_COLUMNS = ['Unique Goal ID', 'Target Start Date', 'Goal Values']


def validate_date(date_str: str) -> Tuple[bool, str]:
    """Validate date format and that it's a Monday."""
    try:
        dt = datetime.strptime(date_str, '%Y-%m-%d')
        if dt.weekday() != 0:  # 0 = Monday
            return False, f"Not a Monday: {date_str} is a {dt.strftime('%A')}"
        return True, ""
    except ValueError:
        return False, f"Invalid date format: {date_str} (expected YYYY-MM-DD)"


def validate_value(value_str: str, metric: str) -> Tuple[bool, str]:
    """Validate value format."""
    try:
        val = float(value_str)
        if val < 0:
            return False, f"Negative value: {value_str}"
        
        # Check decimal places
        if '.' in value_str:
            decimals = len(value_str.split('.')[1])
            if metric == 'AHT':
                if decimals > 3:
                    return False, f"Too many decimals for AHT: {value_str}"
            else:
                if decimals != 3:
                    return False, f"Expected 3 decimals for {metric}: {value_str}"
        
        return True, ""
    except ValueError:
        return False, f"Invalid number: {value_str}"


def validate_upload(filepath: str, existing_filepath: str = None) -> Dict:
    """
    Validate an upload CSV file.
    
    Returns dict with validation results.
    """
    results = {
        'valid': True,
        'errors': [],
        'warnings': [],
        'stats': {}
    }
    
    # Load existing Goal IDs if provided
    existing_keys: Set[str] = set()
    if existing_filepath:
        try:
            with open(existing_filepath, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    goal_id = row.get('Unique Goal ID', '').strip()
                    date = row.get('Target Start Date', '').strip()
                    if goal_id and date:
                        existing_keys.add(f"{goal_id}|{date}")
        except Exception as e:
            results['warnings'].append(f"Could not load existing file: {e}")
    
    # Load and validate upload file
    try:
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            
            # Check required columns
            if reader.fieldnames:
                missing_cols = [c for c in REQUIRED_COLUMNS if c not in reader.fieldnames]
                if missing_cols:
                    results['valid'] = False
                    results['errors'].append(f"Missing required columns: {missing_cols}")
                    return results
            
            rows = list(reader)
    except Exception as e:
        results['valid'] = False
        results['errors'].append(f"Could not read file: {e}")
        return results
    
    results['stats']['total_rows'] = len(rows)
    
    # Track for validation
    seen_keys: Set[str] = set()
    goal_values: Dict[str, List[Tuple[str, float]]] = defaultdict(list)  # goal_id -> [(date, value), ...]
    quarters: Dict[str, int] = defaultdict(int)
    
    for i, row in enumerate(rows, 1):
        goal_id = row.get('Unique Goal ID', '').strip()
        date = row.get('Target Start Date', '').strip()
        value = row.get('Goal Values', '').strip()
        
        # Validate Goal ID
        if not goal_id:
            results['errors'].append(f"Row {i}: Empty Goal ID")
            results['valid'] = False
            continue
        
        parsed = parse_goal_id(goal_id)
        if not parsed:
            results['errors'].append(f"Row {i}: Invalid Goal ID format: {goal_id}")
            results['valid'] = False
            continue
        
        # Track quarter
        quarters[parsed.quarter] += 1
        
        # Validate date
        valid, msg = validate_date(date)
        if not valid:
            results['errors'].append(f"Row {i}: {msg}")
            results['valid'] = False
        
        # Validate value
        valid, msg = validate_value(value, parsed.metric)
        if not valid:
            results['errors'].append(f"Row {i}: {msg}")
            results['valid'] = False
        
        # Check for duplicates within upload
        key = f"{goal_id}|{date}"
        if key in seen_keys:
            results['errors'].append(f"Row {i}: Duplicate (Goal ID + Date): {goal_id}, {date}")
            results['valid'] = False
        seen_keys.add(key)
        
        # Check for duplicates against existing
        if key in existing_keys:
            results['warnings'].append(f"Row {i}: Already exists in Sigma: {goal_id}, {date}")
        
        # Track values for direction validation
        try:
            goal_values[goal_id].append((date, float(value)))
        except ValueError:
            pass
    
    # Check week counts per Goal ID
    goal_week_counts = {gid: len(vals) for gid, vals in goal_values.items()}
    unusual_counts = {gid: cnt for gid, cnt in goal_week_counts.items() if cnt != 13}
    if unusual_counts:
        for gid, cnt in list(unusual_counts.items())[:5]:
            results['warnings'].append(f"Unexpected week count for {gid}: {cnt} (expected 13)")
        if len(unusual_counts) > 5:
            results['warnings'].append(f"...and {len(unusual_counts) - 5} more with unusual counts")
    
    # Validate walk directions
    direction_errors = []
    for goal_id, vals in goal_values.items():
        if len(vals) < 2:
            continue
        
        # Sort by date
        sorted_vals = sorted(vals, key=lambda x: x[0])
        first_val = sorted_vals[0][1]
        last_val = sorted_vals[-1][1]
        
        parsed = parse_goal_id(goal_id)
        if not parsed:
            continue
        
        metric = parsed.metric
        
        if metric in ('DWR', 'FCR'):
            if last_val < first_val:
                direction_errors.append(f"{goal_id}: {metric} walks DOWN ({first_val:.3f} → {last_val:.3f})")
        elif metric == 'AHT':
            if last_val > first_val:
                direction_errors.append(f"{goal_id}: AHT walks UP ({first_val:.2f} → {last_val:.2f})")
    
    if direction_errors:
        results['valid'] = False
        for err in direction_errors[:10]:
            results['errors'].append(f"Wrong direction: {err}")
        if len(direction_errors) > 10:
            results['errors'].append(f"...and {len(direction_errors) - 10} more direction errors")
    
    # Stats
    results['stats']['unique_goal_ids'] = len(goal_values)
    results['stats']['quarters'] = dict(quarters)
    results['stats']['duplicate_within_upload'] = len(seen_keys) - len(goal_values) * 13  # approximate
    results['stats']['would_duplicate_existing'] = sum(1 for k in seen_keys if k in existing_keys)
    
    return results


def main():
    parser = argparse.ArgumentParser(description='Validate Sigma upload CSV')
    parser.add_argument('filepath', help='CSV file to validate')
    parser.add_argument('--existing', '-e', help='Existing Sigma export to check for duplicates')
    parser.add_argument('--json', '-j', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    results = validate_upload(args.filepath, args.existing)
    
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        # Human-readable output
        print(f"{'✓ VALID' if results['valid'] else '✗ INVALID'}")
        print(f"\nStats:")
        for k, v in results['stats'].items():
            print(f"  {k}: {v}")
        
        if results['errors']:
            print(f"\nErrors ({len(results['errors'])}):")
            for err in results['errors'][:20]:
                print(f"  ✗ {err}")
            if len(results['errors']) > 20:
                print(f"  ... and {len(results['errors']) - 20} more errors")
        
        if results['warnings']:
            print(f"\nWarnings ({len(results['warnings'])}):")
            for warn in results['warnings'][:10]:
                print(f"  ⚠ {warn}")
            if len(results['warnings']) > 10:
                print(f"  ... and {len(results['warnings']) - 10} more warnings")
    
    sys.exit(0 if results['valid'] else 1)


if __name__ == '__main__':
    main()
