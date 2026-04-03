TEST_CASES = [
    {
        # Each claim requires a different skill — only one specialist qualifies each time.
        "description": "Disjoint skills, one specialist per claim",
        "fn": "assign_claims",
        "args": [
            [
                {"claim_id": "C1", "complexity": 5, "required_skills": {"python"}},
                {"claim_id": "C2", "complexity": 3, "required_skills": {"java"}},
            ],
            [
                {"specialist_id": "alice", "skills": {"python"}, "current_load": 0},
                {"specialist_id": "bob",   "skills": {"java"},   "current_load": 0},
            ],
        ],
        "expected": {"C1": "alice", "C2": "bob"},
    },
    {
        # Both specialists can handle both claims. Greedy min-load + lex tie-break.
        # C1: alice=0, bob=0  → alice (lex), alice load → 3
        # C2: alice=3, bob=0  → bob,           bob load → 2
        "description": "Load balancing across two claims",
        "fn": "assign_claims",
        "args": [
            [
                {"claim_id": "C1", "complexity": 3, "required_skills": {"python"}},
                {"claim_id": "C2", "complexity": 2, "required_skills": {"python"}},
            ],
            [
                {"specialist_id": "alice", "skills": {"python"}, "current_load": 0},
                {"specialist_id": "bob",   "skills": {"python"}, "current_load": 0},
            ],
        ],
        "expected": {"C1": "alice", "C2": "bob"},
    },
    {
        # Tie-break by specialist_id when loads are equal throughout.
        # "anna" < "bob" < "carol" lexicographically.
        # All have load 0 and all skills → anna always wins every claim.
        "description": "Lexicographic tie-break — same load throughout",
        "fn": "assign_claims",
        "args": [
            [
                {"claim_id": "C1", "complexity": 1, "required_skills": {"x"}},
                {"claim_id": "C2", "complexity": 1, "required_skills": {"x"}},
            ],
            [
                {"specialist_id": "carol", "skills": {"x"}, "current_load": 0},
                {"specialist_id": "anna",  "skills": {"x"}, "current_load": 0},
                {"specialist_id": "bob",   "skills": {"x"}, "current_load": 0},
            ],
        ],
        "expected": {"C1": "anna", "C2": "anna"},
    },
    {
        # Specialist with a non-zero starting load should be skipped
        # in favour of the unloaded one even if lex-larger.
        # C1: zara=0, bob=5 → zara (lower load)
        # C2: zara=4, bob=5 → zara (still lower)
        "description": "Pre-existing load influences assignment",
        "fn": "assign_claims",
        "args": [
            [
                {"claim_id": "C1", "complexity": 4, "required_skills": {"sql"}},
                {"claim_id": "C2", "complexity": 3, "required_skills": {"sql"}},
            ],
            [
                {"specialist_id": "zara", "skills": {"sql"}, "current_load": 0},
                {"specialist_id": "bob",  "skills": {"sql"}, "current_load": 5},
            ],
        ],
        "expected": {"C1": "zara", "C2": "zara"},
    },
    {
        # A claim requires multiple skills. Only specialists with ALL of them qualify.
        # carol has {python, ml, sql}, alice has {python}, bob has {ml, sql}
        # C1 needs {python, ml} → only carol qualifies
        # C2 needs {sql}        → bob and carol qualify; bob load=0, carol load=6 → bob
        # C3 needs {python}     → alice and carol; alice=0, carol=6 → alice
        "description": "Multi-skill requirement filters candidates",
        "fn": "assign_claims",
        "args": [
            [
                {"claim_id": "C1", "complexity": 6, "required_skills": {"python", "ml"}},
                {"claim_id": "C2", "complexity": 2, "required_skills": {"sql"}},
                {"claim_id": "C3", "complexity": 4, "required_skills": {"python"}},
            ],
            [
                {"specialist_id": "alice", "skills": {"python"},          "current_load": 0},
                {"specialist_id": "bob",   "skills": {"ml", "sql"},       "current_load": 0},
                {"specialist_id": "carol", "skills": {"python", "ml", "sql"}, "current_load": 0},
            ],
        ],
        "expected": {"C1": "carol", "C2": "bob", "C3": "alice"},
    },
    {
        # A claim with an empty required_skills set — every specialist is eligible.
        "description": "No required skills — any specialist can take the claim",
        "fn": "assign_claims",
        "args": [
            [
                {"claim_id": "C1", "complexity": 2, "required_skills": set()},
            ],
            [
                {"specialist_id": "beta",  "skills": {"python"}, "current_load": 3},
                {"specialist_id": "alpha", "skills": {"java"},   "current_load": 3},
            ],
        ],
        "expected": {"C1": "alpha"},  # tied load, lex winner
    },
    {
        # Three claims, three specialists — round-robin-like balancing emerges.
        # All start at 0, all have skill "x".
        # C1(5): anna(lex) → anna=5
        # C2(5): bob=0, carol=0, anna=5 → bob (lex of {bob,carol}) → bob=5
        # C3(5): carol=0 → carol → carol=5
        "description": "Three-way round-robin balancing",
        "fn": "assign_claims",
        "args": [
            [
                {"claim_id": "C1", "complexity": 5, "required_skills": {"x"}},
                {"claim_id": "C2", "complexity": 5, "required_skills": {"x"}},
                {"claim_id": "C3", "complexity": 5, "required_skills": {"x"}},
            ],
            [
                {"specialist_id": "carol", "skills": {"x"}, "current_load": 0},
                {"specialist_id": "anna",  "skills": {"x"}, "current_load": 0},
                {"specialist_id": "bob",   "skills": {"x"}, "current_load": 0},
            ],
        ],
        "expected": {"C1": "anna", "C2": "bob", "C3": "carol"},
    },
]
