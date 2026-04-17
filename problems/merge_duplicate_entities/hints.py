HINT = {
    "approach": "Union-Find keyed on IDs, grouping entities transitively",
    "time_complexity": "O(n * k * α(n))  — n entities, k avg IDs each, α ≈ constant",
    "space_complexity": "O(n * k)  — storing all IDs and UF structures",
    "reasoning": """
1. Parse each record to extract (name, list_of_ids).

2. Use Union-Find (disjoint set) keyed on entity indices.
   Maintain a mapping: id_string → first entity index that uses it.

3. For each entity at index i, iterate its IDs:
   - If the ID has been seen before (mapped to entity j), union(i, j).
   - Otherwise, map the ID to entity i.

4. After processing all entities, group them by their UF root.
   For each group:
   - Name = name of the entity with the smallest original index.
   - IDs  = sorted union of all IDs across the group.

5. Sort the final list by name.

Union-Find with path compression and union by rank gives
near-constant amortised time per operation, making this
approach essentially linear in the total number of IDs.

Common mistake: using only pairwise ID comparison (O(n^2))
instead of mapping each ID to its first owner and unioning
on collision — the mapping approach is both simpler and faster.
""",
}
