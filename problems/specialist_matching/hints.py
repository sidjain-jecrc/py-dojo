HINT = {
    "approach": "Greedy earliest-start with interval splitting",
    "time_complexity": "O(t × s × i)  — t tasks, s specialists, i intervals per specialist",
    "space_complexity": "O(s × i)",
    "reasoning": """
Sort tasks by (preferred_start, task_id) once up front.

For each task, iterate over qualified specialists (those with
the required skill). For each specialist, scan their sorted
intervals to find the earliest slot where:

    max(interval_start, preferred_start) + duration <= interval_end

The candidate start for that interval is max(interval_start, preferred_start).
Track the global best (earliest candidate_start, then lex specialist_id).

Once the best assignment is chosen, update that specialist's
intervals by splitting: replace [s, e] with [s, assigned_start]
and [assigned_end, e], discarding zero-length fragments.

Keeping intervals sorted and merging when splitting stays O(i)
per update. For production scale, a segment tree or interval
tree reduces this to O(log i), but the greedy scan is correct
and readable at interview scale.
""",
}
