TEST_CASES = [
    # ----------------------------------------------------------------
    # Part 1: validate_workflow — returns True / False
    # ----------------------------------------------------------------
    {
        # Linear chain: intake → review → approve → close
        "description": "Linear chain — feasible",
        "fn": "validate_workflow",
        "args": [
            ["intake", "review", "approve", "close"],
            [("review", "intake"), ("approve", "review"), ("close", "approve")],
        ],
        "expected": True,
    },
    {
        # Direct two-node cycle: A → B → A
        "description": "Direct two-node cycle — infeasible",
        "fn": "validate_workflow",
        "args": [
            ["A", "B", "C"],
            [("B", "A"), ("A", "B"), ("C", "A")],
        ],
        "expected": False,
    },
    {
        # No dependencies at all — always feasible
        "description": "No dependencies — feasible",
        "fn": "validate_workflow",
        "args": [
            ["intake", "review", "close"],
            [],
        ],
        "expected": True,
    },
    {
        # Single task, no dependencies
        "description": "Single task — feasible",
        "fn": "validate_workflow",
        "args": [
            ["only_task"],
            [],
        ],
        "expected": True,
    },
    {
        # Diamond: A → B, A → C, B → D, C → D
        "description": "Diamond dependency graph — feasible",
        "fn": "validate_workflow",
        "args": [
            ["A", "B", "C", "D"],
            [("B", "A"), ("C", "A"), ("D", "B"), ("D", "C")],
        ],
        "expected": True,
    },
    {
        # Three-node indirect cycle: X → Y → Z → X
        "description": "Indirect three-node cycle — infeasible",
        "fn": "validate_workflow",
        "args": [
            ["X", "Y", "Z"],
            [("Y", "X"), ("Z", "Y"), ("X", "Z")],
        ],
        "expected": False,
    },
    {
        # A task that depends on itself
        "description": "Self-loop — infeasible",
        "fn": "validate_workflow",
        "args": [
            ["T1", "T2"],
            [("T1", "T1"), ("T2", "T1")],
        ],
        "expected": False,
    },
    {
        # Two separate linear chains with no shared dependencies
        "description": "Two independent chains — feasible",
        "fn": "validate_workflow",
        "args": [
            ["p1", "p2", "p3", "q1", "q2"],
            [("p2", "p1"), ("p3", "p2"), ("q2", "q1")],
        ],
        "expected": True,
    },

    # ----------------------------------------------------------------
    # Part 2 (bonus): execution_order — returns list | None
    # Each case below has EXACTLY ONE valid topological order so the
    # result can be compared directly.
    # ----------------------------------------------------------------
    {
        # Linear chain has exactly one valid order
        "description": "Bonus: linear chain — unique execution order",
        "fn": "execution_order",
        "args": [
            ["intake", "review", "approve", "close"],
            [("review", "intake"), ("approve", "review"), ("close", "approve")],
        ],
        "expected": ["intake", "review", "approve", "close"],
    },
    {
        # Single task — trivial order
        "description": "Bonus: single task — order is the task itself",
        "fn": "execution_order",
        "args": [
            ["only_task"],
            [],
        ],
        "expected": ["only_task"],
    },
    {
        # Five-task strict chain — one valid order
        "description": "Bonus: five-task strict chain — unique order",
        "fn": "execution_order",
        "args": [
            ["a", "b", "c", "d", "e"],
            [("b", "a"), ("c", "b"), ("d", "c"), ("e", "d")],
        ],
        "expected": ["a", "b", "c", "d", "e"],
    },
    {
        # Cycle — must return None
        "description": "Bonus: cycle — returns None",
        "fn": "execution_order",
        "args": [
            ["X", "Y", "Z"],
            [("Y", "X"), ("Z", "Y"), ("X", "Z")],
        ],
        "expected": None,
    },
]
