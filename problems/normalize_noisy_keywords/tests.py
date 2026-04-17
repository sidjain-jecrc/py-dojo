TEST_CASES = [
    {
        # Direct single edit: insert 'o' to turn "flod" into "flood".
        "description": "Single insertion — flod to flood",
        "fn": "normalize_keyword",
        "args": ["flod", "flood", ["flood", "floor", "blood", "floods"]],
        "expected": 1,
    },
    {
        # Classic word ladder: hit → hot → dot → dog → cog (4 substitutions).
        "description": "Classic word ladder — hit to cog in 4 steps",
        "fn": "normalize_keyword",
        "args": ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]],
        "expected": 4,
    },
    {
        # No single-edit path exists between "abc" and "xyz".
        "description": "No valid path — returns -1",
        "fn": "normalize_keyword",
        "args": ["abc", "xyz", ["xyz"]],
        "expected": -1,
    },
    {
        # Begin already equals end — zero edits needed.
        "description": "Begin equals end — 0 steps",
        "fn": "normalize_keyword",
        "args": ["flood", "flood", ["flood"]],
        "expected": 0,
    },
    {
        # Two insertions needed: flo → flod → flood (or flo → floo → flood).
        "description": "Two-step path with insertions",
        "fn": "normalize_keyword",
        "args": ["flo", "flood", ["flod", "flood", "floo"]],
        "expected": 2,
    },
    {
        # Direct substitution: a → c in one step.
        "description": "Single-character substitution",
        "fn": "normalize_keyword",
        "args": ["a", "c", ["b", "c"]],
        "expected": 1,
    },
    {
        # Deletion: remove 's' from "floods" to reach "flood".
        "description": "Single deletion — floods to flood",
        "fn": "normalize_keyword",
        "args": ["floods", "flood", ["flood", "floor"]],
        "expected": 1,
    },
    {
        # Direct substitution: cat → bat.
        "description": "Direct one-step substitution — cat to bat",
        "fn": "normalize_keyword",
        "args": ["cat", "bat", ["bat"]],
        "expected": 1,
    },
    {
        # Dictionary has stepping stones but none connect begin to end.
        "description": "Stepping stones exist but path is broken — returns -1",
        "fn": "normalize_keyword",
        "args": ["aaa", "zzz", ["aab", "zzz"]],
        "expected": -1,
    },
]
