HINT = {
    "approach": "Parse → group by ID → sort each group → single-pass merge",
    "time_complexity": "O(n log n)  — dominated by sorting intervals per group",
    "space_complexity": "O(n)  — storing all parsed intervals and merged results",
    "reasoning": """
1. Parse each string to extract (incident_id, start, end).
   A simple split or regex works — the format is fixed.

2. Group intervals into a dict: incident_id → list of (start, end).

3. For each incident, sort its intervals by start time.

4. Merge with a single pass:
   - Initialise merged list with the first interval.
   - For each subsequent interval, compare its start with the
     end of the last merged interval:
       * If last_end + 1 >= current_start → overlap or adjacent,
         extend: last_end = max(last_end, current_end).
       * Otherwise → gap, append a new interval.

5. Build the result dict with keys in sorted order.

The key insight is that after sorting by start, you only need
to compare each interval against the most recent merged interval.
Sorting guarantees that no earlier interval can extend past
one you've already processed.

Common mistake: forgetting to handle adjacency (end+1 == start)
as a merge case, or not taking max(last_end, current_end) when
merging (a later-starting interval can end before the current
merged interval's end).
""",
}
