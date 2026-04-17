TEST_CASES = [
    {
        # The example from the problem description.
        # All four intervals for incident A merge into one.
        "description": "All intervals merge into one (overlap + adjacency)",
        "fn": "consolidate_timelines",
        "args": [[
            "incident=A, start=10, end=15",
            "incident=A, start=12, end=18",
            "incident=A, start=20, end=25",
            "incident=A, start=17, end=19",
        ]],
        "expected": {"A": [(10, 25)]},
    },
    {
        # Two incidents with independent interval sets.
        "description": "Multiple incidents — grouped and merged independently",
        "fn": "consolidate_timelines",
        "args": [[
            "incident=A, start=1, end=5",
            "incident=B, start=2, end=6",
            "incident=A, start=4, end=8",
            "incident=B, start=10, end=15",
        ]],
        "expected": {
            "A": [(1, 8)],
            "B": [(2, 6), (10, 15)],
        },
    },
    {
        # Three intervals for the same incident, none overlapping or adjacent.
        "description": "No overlapping intervals — all remain separate",
        "fn": "consolidate_timelines",
        "args": [[
            "incident=X, start=1, end=3",
            "incident=X, start=10, end=12",
            "incident=X, start=20, end=22",
        ]],
        "expected": {"X": [(1, 3), (10, 12), (20, 22)]},
    },
    {
        # Chain of overlapping intervals that cascade into one.
        "description": "Cascading overlaps — all collapse into one interval",
        "fn": "consolidate_timelines",
        "args": [[
            "incident=Z, start=1, end=10",
            "incident=Z, start=5, end=15",
            "incident=Z, start=12, end=20",
        ]],
        "expected": {"Z": [(1, 20)]},
    },
    {
        "description": "Empty input",
        "fn": "consolidate_timelines",
        "args": [[]],
        "expected": {},
    },
    {
        "description": "Single report — returned as-is",
        "fn": "consolidate_timelines",
        "args": [["incident=A, start=5, end=10"]],
        "expected": {"A": [(5, 10)]},
    },
    {
        # Adjacent means end+1 == start of next → should merge.
        "description": "Adjacent intervals merge (end+1 == next start)",
        "fn": "consolidate_timelines",
        "args": [[
            "incident=A, start=1, end=5",
            "incident=A, start=6, end=10",
        ]],
        "expected": {"A": [(1, 10)]},
    },
    {
        # Gap of 2 between intervals — should NOT merge.
        "description": "Gap of 2 between intervals — no merge",
        "fn": "consolidate_timelines",
        "args": [[
            "incident=A, start=1, end=5",
            "incident=A, start=7, end=10",
        ]],
        "expected": {"A": [(1, 5), (7, 10)]},
    },
    {
        # Multiple incidents, some with merges, some without.
        "description": "Complex mix — multiple incidents with varied merges",
        "fn": "consolidate_timelines",
        "args": [[
            "incident=SRV, start=0, end=5",
            "incident=SRV, start=3, end=8",
            "incident=SRV, start=15, end=20",
            "incident=DB, start=2, end=10",
            "incident=DB, start=11, end=14",
            "incident=DB, start=18, end=25",
        ]],
        "expected": {
            "DB":  [(2, 14), (18, 25)],
            "SRV": [(0, 8), (15, 20)],
        },
    },
    {
        # Two identical intervals — collapse to one.
        "description": "Duplicate intervals merge into one",
        "fn": "consolidate_timelines",
        "args": [[
            "incident=A, start=5, end=10",
            "incident=A, start=5, end=10",
        ]],
        "expected": {"A": [(5, 10)]},
    },
]
