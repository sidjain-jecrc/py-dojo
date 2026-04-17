TEST_CASES = [
    {
        # (2,1) → (2,0) → (3,0)=I  — 2 steps.
        "description": "Basic grid — nearest incident is 2 steps away",
        "fn": "nearest_incident",
        "args": [
            [
                ["E", "E", "B", "I"],
                ["B", "E", "B", "E"],
                ["E", "E", "E", "E"],
                ["I", "B", "E", "E"],
            ],
            [2, 1],
        ],
        "expected": 2,
    },
    {
        # (0,0) → (0,1)=I  — 1 step.
        "description": "Incident immediately adjacent",
        "fn": "nearest_incident",
        "args": [
            [["E", "I"], ["E", "E"]],
            [0, 0],
        ],
        "expected": 1,
    },
    {
        # Start cell is itself an incident.
        "description": "Start is on an incident — 0 steps",
        "fn": "nearest_incident",
        "args": [
            [["I"]],
            [0, 0],
        ],
        "expected": 0,
    },
    {
        # Start is completely walled in by B cells.
        "description": "Start blocked in — no reachable incident",
        "fn": "nearest_incident",
        "args": [
            [
                ["E", "B", "I"],
                ["B", "B", "B"],
                ["E", "E", "E"],
            ],
            [0, 0],
        ],
        "expected": -1,
    },
    {
        # No incident cells exist anywhere.
        "description": "No incidents on the grid",
        "fn": "nearest_incident",
        "args": [
            [["E", "E"], ["E", "E"]],
            [0, 0],
        ],
        "expected": -1,
    },
    {
        # Row 1 is almost entirely blocked; must go the long way around.
        # (2,0)→(2,1)→(2,2)→(2,3)→(2,4)→(1,4)→(0,4)=I  — 6 steps.
        "description": "Must navigate around a wall of blocked cells",
        "fn": "nearest_incident",
        "args": [
            [
                ["I", "E", "E", "E", "I"],
                ["B", "B", "B", "B", "E"],
                ["E", "E", "E", "E", "E"],
            ],
            [2, 0],
        ],
        "expected": 6,
    },
    {
        # Single row, straight line to the incident.
        # (0,0)→(0,1)→(0,2)→(0,3)=I  — 3 steps.
        "description": "Straight-line path in single row",
        "fn": "nearest_incident",
        "args": [
            [["E", "E", "E", "I"]],
            [0, 0],
        ],
        "expected": 3,
    },
    {
        # Single row with a blocker in the way — path is severed.
        "description": "Blocked path in single row — unreachable",
        "fn": "nearest_incident",
        "args": [
            [["E", "B", "E", "I"]],
            [0, 0],
        ],
        "expected": -1,
    },
    {
        # Diagonal traversal across open grid.
        # (0,0)→(0,1)→(0,2)→(1,2)→(2,2)=I or similar — 4 steps.
        "description": "Open grid — diagonal-like traversal",
        "fn": "nearest_incident",
        "args": [
            [
                ["E", "E", "E"],
                ["E", "E", "E"],
                ["E", "E", "I"],
            ],
            [0, 0],
        ],
        "expected": 4,
    },
    {
        # Multiple incidents at different distances — nearest wins.
        "description": "Multiple incidents — closest one wins",
        "fn": "nearest_incident",
        "args": [
            [
                ["I", "I"],
                ["I", "E"],
            ],
            [1, 1],
        ],
        "expected": 1,
    },
]
