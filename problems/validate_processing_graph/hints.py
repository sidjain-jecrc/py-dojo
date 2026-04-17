HINT = {
    "approach": "Union-Find: process edges, check n nodes, n-1 edges, no cycles",
    "time_complexity": "O(E * α(n))  — nearly linear in the number of edges",
    "space_complexity": "O(n)  — Union-Find parent and rank arrays",
    "reasoning": """
A graph with n nodes is a valid tree if and only if it has
exactly n-1 edges AND is connected AND has no cycles. Any two
of these three properties imply the third, but checking all
three makes the logic clear.

Union-Find approach:
1. Parse each "X->Y" edge to extract two node names.
2. Collect all distinct nodes. If count != n, return False.
3. If edge count != n - 1, return False.
4. Initialise Union-Find over all nodes.
5. For each edge (u, v):
   - If u == v (self-loop), return False.
   - If find(u) == find(v), a cycle exists → return False.
   - Otherwise, union(u, v).
6. After all edges, check that all nodes share the same root
   (single connected component). If so, return True.

With path compression and union by rank, each find/union is
amortised O(α(n)) ≈ O(1).

Alternative: BFS/DFS from any node after building an adjacency
list — if you visit all n nodes without revisiting any, it's a
tree.

Common mistake: forgetting to check that the number of distinct
nodes matches n, or not handling self-loops as an automatic
failure.
""",
}
