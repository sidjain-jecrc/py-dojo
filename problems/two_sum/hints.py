HINT = {
    "approach": "Single-pass hash map",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "reasoning": """
Store each number's index in a dict as you iterate.
For each element x, check whether (target - x) is already
in the dict — if yes, you have your pair in O(1) lookup.

This avoids the O(n²) cost of a nested loop that checks
every pair. The trade-off is O(n) extra space for the dict,
which is almost always worth it.
""",
}
