HINT = {
    "approach": "Single-pass grouping with per-case running state",
    "time_complexity": "O(n)  — n events",
    "space_complexity": "O(c)  — c unique cases",
    "reasoning": """
Iterate through events once, accumulating state per case_id
in a dict: track the latest (timestamp, event_type) pair and
a running count of high-severity events.

Comparing timestamps as ISO 8601 strings works correctly with
a plain lexicographic comparison (str > str) because the
format is zero-padded and sortable by design — no datetime
parsing needed.

Apply escalation rules only after the single pass, keeping
the logic clean and the overall complexity O(n).
""",
}
