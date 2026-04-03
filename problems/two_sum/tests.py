TEST_CASES = [
    {
        "description": "Basic case",
        "fn": "solve",
        "args": [[2, 7, 11, 15], 9],
        "expected": [0, 1],
    },
    {
        "description": "Target at end of list",
        "fn": "solve",
        "args": [[3, 2, 4], 6],
        "expected": [1, 2],
    },
    {
        "description": "Duplicate values",
        "fn": "solve",
        "args": [[3, 3], 6],
        "expected": [0, 1],
    },
    {
        "description": "Negative numbers",
        "fn": "solve",
        "args": [[-1, -2, -3, -4, -5], -8],
        "expected": [2, 4],
    },
    {
        "description": "Single pair in longer list",
        "fn": "solve",
        "args": [[1, 5, 3, 8, 2], 10],
        "expected": [3, 4],
    },
]
