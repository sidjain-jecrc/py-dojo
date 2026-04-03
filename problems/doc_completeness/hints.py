HINT = {
    "approach": "Set difference after building required-doc set",
    "time_complexity": "O(r + u)  — r required docs, u uploaded docs",
    "space_complexity": "O(r + u)",
    "reasoning": """
Collect all required documents into a set, then convert the
uploaded list to a set and compute the difference:

    missing = required - uploaded_set

Set difference is O(r + u) and produces the answer in one
operation, avoiding an explicit loop over required docs.

Sort the missing set before returning so the output is
deterministic regardless of the order rules are evaluated in.
""",
}
