HINT = {
    "approach": "Post-order DFS — compute children before parent",
    "time_complexity": "O(n)  — n nodes in the tree",
    "space_complexity": "O(d)  — d is the depth of the tree (call stack)",
    "reasoning": """
Recurse into each child first (post-order), collect their subtree
totals, then compute the current node's total as:

    node_total = base_exposure + sum(child_totals)

Store the result in a dict as you return up the call stack.
Each node is visited exactly once → O(n).

An iterative approach with an explicit stack avoids Python's
recursion limit for very deep trees, using the same post-order
logic: push nodes onto the stack and process children before
parents.
""",
}
