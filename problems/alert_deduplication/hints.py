HINT = {
    "approach": "Sort once, then a single pass with a last-emitted dict",
    "time_complexity": "O(n log n)  — dominated by the sort",
    "space_complexity": "O(k)  — k unique (tenant_id, alert_type) pairs",
    "reasoning": """
Sort all alerts by (timestamp, tenant_id, alert_type) once.

Maintain a dict:  last_emitted[(tenant_id, alert_type)] = timestamp

For each alert in sorted order:
  - Look up the last emitted timestamp for this (tenant, type).
  - If no previous emit, or gap > 15 → emit the alert and update last_emitted.
  - Otherwise → increment suppressed_count.

One pass after sorting → O(n) for the scan, O(n log n) overall.

The common mistake is comparing against the first-ever alert
instead of the last-emitted one — that would give wrong results
when a long-running stream produces many windows for the same
(tenant, type) pair.
""",
}
