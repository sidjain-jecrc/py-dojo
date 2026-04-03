HINT = {
    "approach": "Kahn's algorithm — BFS-based topological sort",
    "time_complexity": "O(V + E)  — V tasks, E dependencies",
    "space_complexity": "O(V + E)",
    "reasoning": """
Build an adjacency list and an in-degree count for every node.
Seed a queue with all nodes whose in-degree is 0 (no prerequisites).
Repeatedly dequeue a node, append it to the result, and decrement
the in-degree of its dependents — re-enqueue any that reach 0.

If the final result contains all V tasks the graph is acyclic
(feasible). If any nodes remain with non-zero in-degree, they
are part of a cycle (infeasible) — return None for the order.

This is preferable to DFS cycle detection because it produces
the topological order as a natural by-product and is easier to
reason about iteratively without a visited-colour state machine.
""",
}
