TEST_CASES = [
    {
        # Linear chain: A—B—C—D. 4 nodes, 3 edges, connected, no cycle.
        "description": "Valid tree — linear chain",
        "fn": "validate_graph",
        "args": [4, ["A->B", "B->C", "C->D"]],
        "expected": True,
    },
    {
        # Star topology: HUB at center. 4 nodes, 3 edges, connected, no cycle.
        "description": "Valid tree — star topology",
        "fn": "validate_graph",
        "args": [4, ["HUB->A", "HUB->B", "HUB->C"]],
        "expected": True,
    },
    {
        # Triangle: 3 nodes, 3 edges (not n-1=2), forms a cycle.
        "description": "Cycle — triangle is not a tree",
        "fn": "validate_graph",
        "args": [3, ["A->B", "B->C", "C->A"]],
        "expected": False,
    },
    {
        # Two disconnected pairs: 4 nodes but only 2 edges (not n-1=3).
        "description": "Disconnected components — not a tree",
        "fn": "validate_graph",
        "args": [4, ["A->B", "C->D"]],
        "expected": False,
    },
    {
        # Square with extra diagonal: 4 nodes, 4 edges (not n-1=3), has cycle.
        "description": "Extra edge creates cycle — not a tree",
        "fn": "validate_graph",
        "args": [4, ["A->B", "B->C", "C->D", "D->A"]],
        "expected": False,
    },
    {
        # Edges define 4 nodes but n claims 5 — mismatch.
        "description": "Node count mismatch — fewer nodes than expected",
        "fn": "validate_graph",
        "args": [5, ["A->B", "B->C", "C->D"]],
        "expected": False,
    },
    {
        # Minimal valid tree: 2 nodes, 1 edge.
        "description": "Valid tree — two nodes",
        "fn": "validate_graph",
        "args": [2, ["X->Y"]],
        "expected": True,
    },
    {
        # Self-loop adds an extra edge and creates a cycle.
        "description": "Self-loop — not a tree",
        "fn": "validate_graph",
        "args": [2, ["A->B", "B->B"]],
        "expected": False,
    },
    {
        # Full binary tree: 7 nodes, 6 edges, connected, no cycle.
        "description": "Valid tree — binary tree structure",
        "fn": "validate_graph",
        "args": [7, ["A->B", "A->C", "B->D", "B->E", "C->F", "C->G"]],
        "expected": True,
    },
]
