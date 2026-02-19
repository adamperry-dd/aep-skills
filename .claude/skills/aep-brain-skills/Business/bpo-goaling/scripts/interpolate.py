#!/usr/bin/env python3
"""
Interpolate missing Week 1 values in BPO goal data.

Rule: Partner Initiative file often has missing Week 1 (first week of quarter).
We fill it by applying a small backward step from Week 2.

Improvement Direction:
- DWR, FCR: Higher = Better → Week 1 = Week 2 - 0.003
- AHT: Lower = Better → Week 1 = Week 2 + 0.3

Usage:
    python interpolate.py --metric DWR --week2 0.724
    python interpolate.py --file data.csv --metric-column Metric --values-column "Week 1,Week 2,..."
"""

import argparse
import json
import sys
from typing import List, Optional


# Interpolation constants
PERCENTAGE_STEP = 0.003  # For DWR, FCR (percentage metrics)
MINUTES_STEP = 0.3       # For AHT (duration metric)


def interpolate_week1(metric: str, week2_value: float) -> float:
    """
    Calculate Week 1 value based on Week 2 and metric type.
    
    Args:
        metric: 'DWR', 'FCR', or 'AHT'
        week2_value: The Week 2 value
    
    Returns:
        Interpolated Week 1 value
    """
    metric = metric.upper()
    
    if metric in ('DWR', 'FCR'):
        # Percentage metrics: higher = better
        # Week 1 should be LOWER (worse) than Week 2
        return round(week2_value - PERCENTAGE_STEP, 3)
    
    elif metric == 'AHT':
        # Duration metric: lower = better
        # Week 1 should be HIGHER (worse) than Week 2
        return round(week2_value + MINUTES_STEP, 2)
    
    else:
        raise ValueError(f"Unknown metric: {metric}. Expected DWR, FCR, or AHT.")


def interpolate_series(metric: str, values: List[Optional[float]]) -> List[float]:
    """
    Fill None values in a series of weekly values.
    
    Only fills Week 1 (index 0) if Week 2 (index 1) exists.
    
    Args:
        metric: 'DWR', 'FCR', or 'AHT'
        values: List of weekly values (may contain None)
    
    Returns:
        List with interpolated values
    """
    if not values:
        return values
    
    result = values.copy()
    
    # Only interpolate Week 1 if it's None and Week 2 exists
    if len(result) >= 2:
        if result[0] is None and result[1] is not None:
            result[0] = interpolate_week1(metric, result[1])
    
    return result


def validate_walk_direction(metric: str, values: List[float]) -> dict:
    """
    Validate that the walk direction is correct.
    
    Args:
        metric: 'DWR', 'FCR', or 'AHT'
        values: List of weekly values (no None values)
    
    Returns:
        Dict with validation results
    """
    if not values or len(values) < 2:
        return {'valid': True, 'message': 'Insufficient data to validate'}
    
    # Filter out None values
    clean_values = [v for v in values if v is not None]
    if len(clean_values) < 2:
        return {'valid': True, 'message': 'Insufficient non-None values'}
    
    first = clean_values[0]
    last = clean_values[-1]
    
    metric = metric.upper()
    
    if metric in ('DWR', 'FCR'):
        # Should walk UP (higher = better)
        if last >= first:
            return {'valid': True, 'direction': 'UP', 'delta': round(last - first, 4)}
        else:
            return {
                'valid': False, 
                'direction': 'DOWN', 
                'delta': round(last - first, 4),
                'message': f'{metric} should walk UP but walks DOWN ({first} → {last})'
            }
    
    elif metric == 'AHT':
        # Should walk DOWN (lower = better)
        if last <= first:
            return {'valid': True, 'direction': 'DOWN', 'delta': round(last - first, 2)}
        else:
            return {
                'valid': False, 
                'direction': 'UP', 
                'delta': round(last - first, 2),
                'message': f'AHT should walk DOWN but walks UP ({first} → {last})'
            }
    
    else:
        return {'valid': True, 'message': f'Unknown metric: {metric}'}


def main():
    parser = argparse.ArgumentParser(description='Interpolate missing Week 1 values')
    parser.add_argument('--metric', '-m', required=True, 
                        choices=['DWR', 'FCR', 'AHT', 'dwr', 'fcr', 'aht'],
                        help='Metric type')
    parser.add_argument('--week2', '-w', type=float,
                        help='Week 2 value (for single calculation)')
    parser.add_argument('--values', '-v', 
                        help='Comma-separated weekly values (use "None" for missing)')
    parser.add_argument('--validate', action='store_true',
                        help='Also validate walk direction')
    parser.add_argument('--json', '-j', action='store_true',
                        help='Output as JSON')
    
    args = parser.parse_args()
    metric = args.metric.upper()
    
    if args.week2 is not None:
        # Single calculation
        week1 = interpolate_week1(metric, args.week2)
        
        if args.json:
            print(json.dumps({
                'metric': metric,
                'week2': args.week2,
                'week1_interpolated': week1,
                'step': PERCENTAGE_STEP if metric in ('DWR', 'FCR') else MINUTES_STEP
            }, indent=2))
        else:
            print(f"Week 1 (interpolated): {week1}")
            print(f"Week 2: {args.week2}")
            print(f"Step applied: {'-' if metric in ('DWR', 'FCR') else '+'}"
                  f"{PERCENTAGE_STEP if metric in ('DWR', 'FCR') else MINUTES_STEP}")
    
    elif args.values:
        # Series interpolation
        raw_values = args.values.split(',')
        values = []
        for v in raw_values:
            v = v.strip()
            if v.lower() == 'none' or v == '':
                values.append(None)
            else:
                values.append(float(v))
        
        interpolated = interpolate_series(metric, values)
        
        result = {
            'metric': metric,
            'original': values,
            'interpolated': interpolated
        }
        
        if args.validate:
            validation = validate_walk_direction(metric, interpolated)
            result['validation'] = validation
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"Original: {values}")
            print(f"Interpolated: {interpolated}")
            if args.validate:
                v = result['validation']
                if v['valid']:
                    print(f"Direction: {v.get('direction', 'N/A')} ✓")
                else:
                    print(f"Direction: {v.get('direction', 'N/A')} ✗ - {v.get('message', '')}")
    
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
