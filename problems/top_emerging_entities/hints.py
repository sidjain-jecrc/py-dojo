HINT = {
    "approach": "Count with a hash map, then sort by (-frequency, name)",
    "time_complexity": "O(n + d log d)  — n mentions, d distinct entities",
    "space_complexity": "O(d)  — one counter entry per distinct entity",
    "reasoning": """
Use collections.Counter (or a plain dict) to count each entity
in a single O(n) pass.

Sort the distinct entities by (-count, name) so that higher
frequencies come first and ties are broken lexicographically.

Return the first k entries from the sorted list.

Alternative: use a min-heap of size k for O(n + d log k), which
is better when k << d. Python's heapq.nsmallest with the key
(-count, name) does this in one call. For most practical input
sizes the sort approach is simpler and fast enough.

Common mistakes:
  - Forgetting the tiebreaker and returning an unstable order.
  - Using max-heap with default string comparison (descending
    frequency but also descending lex order for ties).
  - Off-by-one when k equals the number of distinct entities.
""",
}
