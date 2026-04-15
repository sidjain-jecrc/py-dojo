TEST_CASES = [
    {
        # Basic example from the problem statement.
        "description": "Basic grouping — two anagram groups",
        "fn": "group_anagrams",
        "args": [
            ["alert", "later", "fire", "rife", "alter"],
        ],
        "expected": [["alert", "alter", "later"], ["fire", "rife"]],
    },
    {
        # No two tokens are anagrams — each token is its own group.
        "description": "No anagrams — every token in its own group",
        "fn": "group_anagrams",
        "args": [
            ["flood", "quake", "storm"],
        ],
        "expected": [["flood"], ["quake"], ["storm"]],
    },
    {
        # All tokens are anagrams of each other — single group.
        "description": "All tokens are anagrams — single group",
        "fn": "group_anagrams",
        "args": [
            ["listen", "silent", "enlist", "tinsel"],
        ],
        "expected": [["enlist", "listen", "silent", "tinsel"]],
    },
    {
        # Single token — one group of one.
        "description": "Single token — one group",
        "fn": "group_anagrams",
        "args": [
            ["tsunami"],
        ],
        "expected": [["tsunami"]],
    },
    {
        # Empty input — no groups.
        "description": "Empty token list — no groups",
        "fn": "group_anagrams",
        "args": [
            [],
        ],
        "expected": [],
    },
    {
        # Duplicate tokens — duplicates stay in the same group.
        "description": "Duplicate tokens appear in the same group",
        "fn": "group_anagrams",
        "args": [
            ["warn", "warn", "wran"],
        ],
        "expected": [["warn", "warn", "wran"]],
    },
    {
        # Different lengths can never be anagrams.
        "description": "Different lengths — separate groups",
        "fn": "group_anagrams",
        "args": [
            ["ab", "abc", "ba", "cab"],
        ],
        "expected": [["ab", "ba"], ["abc", "cab"]],
    },
    {
        # Single-character tokens.
        "description": "Single-character tokens — matching and non-matching",
        "fn": "group_anagrams",
        "args": [
            ["a", "b", "a", "c", "b"],
        ],
        "expected": [["a", "a"], ["b", "b"], ["c"]],
    },
    {
        # Tokens with repeated letters — frequency matters.
        "description": "Repeated letters — frequency distinguishes groups",
        "fn": "group_anagrams",
        "args": [
            ["aab", "aba", "baa", "abb", "bab"],
        ],
        # "aab","aba","baa" all have a=2,b=1; "abb","bab" have a=1,b=2
        "expected": [["aab", "aba", "baa"], ["abb", "bab"]],
    },
    {
        # Realistic noisy alert scenario with multiple groups.
        "description": "Realistic noisy alerts — multiple mixed groups",
        "fn": "group_anagrams",
        "args": [
            [
                "danger", "garden", "gander",
                "nuclear", "unclear",
                "surge",
                "riots", "trios", "trois",
                "blast",
            ],
        ],
        "expected": [
            ["blast"],
            ["danger", "gander", "garden"],
            ["nuclear", "unclear"],
            ["riots", "trios", "trois"],
            ["surge"],
        ],
    },
]
