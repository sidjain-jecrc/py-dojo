HINT = {
    "approach": "Union-Find with index maps for O(1) match lookup",
    "time_complexity": "O(n α(n))  — n records, α is inverse Ackermann (≈ O(1))",
    "space_complexity": "O(n)",
    "reasoning": """
Build three lookup dicts up front — one keyed on phone, one on
email, one on (normalised_name, dob). For each record, check
all three dicts in O(1): if a previous record shares a key,
union the two records in the Union-Find structure.

Union-Find with path compression and union-by-rank makes each
find/union nearly O(1) amortised, giving O(n) overall (ignoring
the α factor which is effectively constant).

The naive alternative — comparing every pair of records — is
O(n²) and becomes expensive quickly as n grows into the tens
of thousands typical of claims databases.
""",
}
