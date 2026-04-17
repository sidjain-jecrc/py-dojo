TEST_CASES = [
    {
        # Airport A and Airport A Duplicate share "KJFK" → merge.
        # Airport B has no overlap → stays separate.
        "description": "Basic merge on shared ID",
        "fn": "merge_entities",
        "args": [[
            "name=Airport A|ids=JFK,KJFK",
            "name=Airport A Duplicate|ids=KJFK,NYC",
            "name=Airport B|ids=LAX",
        ]],
        "expected": [
            {"name": "Airport A", "ids": ["JFK", "KJFK", "NYC"]},
            {"name": "Airport B", "ids": ["LAX"]},
        ],
    },
    {
        # No shared IDs — all entities remain independent.
        "description": "No overlapping IDs — no merges",
        "fn": "merge_entities",
        "args": [[
            "name=A|ids=1,2",
            "name=B|ids=3,4",
        ]],
        "expected": [
            {"name": "A", "ids": ["1", "2"]},
            {"name": "B", "ids": ["3", "4"]},
        ],
    },
    {
        # Transitive chain: X↔Y via 'b', Y↔Z via 'c' → all merge.
        "description": "Transitive merge — chain of shared IDs",
        "fn": "merge_entities",
        "args": [[
            "name=X|ids=a,b",
            "name=Y|ids=b,c",
            "name=Z|ids=c,d",
        ]],
        "expected": [
            {"name": "X", "ids": ["a", "b", "c", "d"]},
        ],
    },
    {
        "description": "Empty input",
        "fn": "merge_entities",
        "args": [[]],
        "expected": [],
    },
    {
        "description": "Single entity — returned as-is",
        "fn": "merge_entities",
        "args": [["name=Solo|ids=X"]],
        "expected": [
            {"name": "Solo", "ids": ["X"]},
        ],
    },
    {
        # C shares id '2' with A and id '3' with B → all three merge.
        "description": "Bridge entity connects two otherwise separate groups",
        "fn": "merge_entities",
        "args": [[
            "name=A|ids=1,2",
            "name=B|ids=3,4",
            "name=C|ids=2,3",
        ]],
        "expected": [
            {"name": "A", "ids": ["1", "2", "3", "4"]},
        ],
    },
    {
        # Multiple independent merge groups.
        "description": "Multiple independent groups merge separately",
        "fn": "merge_entities",
        "args": [[
            "name=A|ids=1",
            "name=B|ids=2",
            "name=C|ids=1",
            "name=D|ids=3",
            "name=E|ids=2",
        ]],
        "expected": [
            {"name": "A", "ids": ["1"]},
            {"name": "B", "ids": ["2"]},
            {"name": "D", "ids": ["3"]},
        ],
    },
    {
        # Large entity absorbs a smaller one via a single shared ID.
        "description": "Large entity absorbs smaller one on single shared ID",
        "fn": "merge_entities",
        "args": [[
            "name=Hub|ids=A,B,C,D",
            "name=Spoke|ids=D,E",
        ]],
        "expected": [
            {"name": "Hub", "ids": ["A", "B", "C", "D", "E"]},
        ],
    },
    {
        # Three entities all pairwise connected — still one group.
        "description": "Three-way pairwise overlap merges into one",
        "fn": "merge_entities",
        "args": [[
            "name=P|ids=x,y",
            "name=Q|ids=y,z",
            "name=R|ids=x,z",
        ]],
        "expected": [
            {"name": "P", "ids": ["x", "y", "z"]},
        ],
    },
]
