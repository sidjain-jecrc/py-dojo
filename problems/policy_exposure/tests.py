TEST_CASES = [
    {
        # Single leaf node — subtree exposure equals base_exposure.
        "description": "Single leaf node",
        "fn": "calculate_exposures",
        "args": [{"policy_id": "P1", "base_exposure": 42, "children": []}],
        "expected": {"P1": 42},
    },
    {
        # Root with two leaf children.
        # root = 10 + 5 + 8 = 23
        "description": "Root with two leaf children",
        "fn": "calculate_exposures",
        "args": [{
            "policy_id": "root", "base_exposure": 10,
            "children": [
                {"policy_id": "A", "base_exposure": 5, "children": []},
                {"policy_id": "B", "base_exposure": 8, "children": []},
            ],
        }],
        "expected": {"root": 23, "A": 5, "B": 8},
    },
    {
        # Three-level tree.
        # C = 8
        # B = 3 + 8 = 11
        # root = 10 + 5 + 11 = 26
        "description": "Three-level tree",
        "fn": "calculate_exposures",
        "args": [{
            "policy_id": "root", "base_exposure": 10,
            "children": [
                {"policy_id": "A", "base_exposure": 5, "children": []},
                {"policy_id": "B", "base_exposure": 3,
                 "children": [
                     {"policy_id": "C", "base_exposure": 8, "children": []},
                 ]},
            ],
        }],
        "expected": {"root": 26, "A": 5, "B": 11, "C": 8},
    },
    {
        # Linear chain: root → child → grandchild → leaf
        # leaf  = 4
        # grand = 3 + 4 = 7
        # child = 2 + 7 = 9
        # root  = 1 + 9 = 10
        "description": "Deep linear chain",
        "fn": "calculate_exposures",
        "args": [{
            "policy_id": "root", "base_exposure": 1,
            "children": [{
                "policy_id": "child", "base_exposure": 2,
                "children": [{
                    "policy_id": "grand", "base_exposure": 3,
                    "children": [
                        {"policy_id": "leaf", "base_exposure": 4, "children": []},
                    ],
                }],
            }],
        }],
        "expected": {"root": 10, "child": 9, "grand": 7, "leaf": 4},
    },
    {
        # Wide root — four leaf children, no grandchildren.
        # root = 1 + 10 + 20 + 30 + 40 = 101
        "description": "Wide root — four leaf children",
        "fn": "calculate_exposures",
        "args": [{
            "policy_id": "root", "base_exposure": 1,
            "children": [
                {"policy_id": "A", "base_exposure": 10, "children": []},
                {"policy_id": "B", "base_exposure": 20, "children": []},
                {"policy_id": "C", "base_exposure": 30, "children": []},
                {"policy_id": "D", "base_exposure": 40, "children": []},
            ],
        }],
        "expected": {"root": 101, "A": 10, "B": 20, "C": 30, "D": 40},
    },
    {
        # Node with zero base_exposure — still accumulates children.
        "description": "Node with zero base_exposure",
        "fn": "calculate_exposures",
        "args": [{
            "policy_id": "root", "base_exposure": 0,
            "children": [
                {"policy_id": "A", "base_exposure": 15, "children": []},
            ],
        }],
        "expected": {"root": 15, "A": 15},
    },
    {
        # Asymmetric tree: left subtree is deeper than right.
        # E = 5
        # C = 2 + 5 = 7
        # A = 10 + 7 = 17
        # B = 8
        # root = 1 + 17 + 8 = 26
        "description": "Asymmetric tree — left subtree deeper",
        "fn": "calculate_exposures",
        "args": [{
            "policy_id": "root", "base_exposure": 1,
            "children": [
                {"policy_id": "A", "base_exposure": 10,
                 "children": [
                     {"policy_id": "C", "base_exposure": 2,
                      "children": [
                          {"policy_id": "E", "base_exposure": 5, "children": []},
                      ]},
                 ]},
                {"policy_id": "B", "base_exposure": 8, "children": []},
            ],
        }],
        "expected": {"root": 26, "A": 17, "B": 8, "C": 7, "E": 5},
    },
]
