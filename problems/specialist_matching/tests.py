TEST_CASES = [
    {
        # Single specialist, single task — fits exactly.
        "description": "Single specialist, single task — exact fit",
        "fn": "assign_tasks",
        "args": [
            [{"specialist_id": "S1", "skills": {"python"}, "available": [[0, 100]]}],
            [{"task_id": "T1", "required_skill": "python", "duration": 30, "preferred_start": 10}],
        ],
        "expected": [("T1", "S1", 10, 40)],
    },
    {
        # Only one specialist has the required skill — other is skipped.
        "description": "Skill filter — only matching specialist is used",
        "fn": "assign_tasks",
        "args": [
            [
                {"specialist_id": "S1", "skills": {"java"},   "available": [[0, 100]]},
                {"specialist_id": "S2", "skills": {"python"}, "available": [[0, 100]]},
            ],
            [{"task_id": "T1", "required_skill": "python", "duration": 20, "preferred_start": 0}],
        ],
        "expected": [("T1", "S2", 0, 20)],
    },
    {
        # Two tasks for one specialist — second uses remaining availability.
        # T1 assigned [10, 40]; S1 availability becomes [[0,10],[40,100]]
        # T2 preferred_start=0, earliest valid slot is [0,10] (duration=5 fits) → start=0
        "description": "Two tasks, one specialist — second uses leftover slot",
        "fn": "assign_tasks",
        "args": [
            [{"specialist_id": "S1", "skills": {"sql"}, "available": [[0, 100]]}],
            [
                {"task_id": "T1", "required_skill": "sql", "duration": 30, "preferred_start": 10},
                {"task_id": "T2", "required_skill": "sql", "duration": 5,  "preferred_start": 0},
            ],
        ],
        # Tasks processed by preferred_start: T2(0) before T1(10)
        # T2: S1 [0,100], preferred=0, start=0, end=5. S1 now [[5,100]]
        # T1: S1 [5,100], preferred=10, start=10, end=40.
        "expected": [("T2", "S1", 0, 5), ("T1", "S1", 10, 40)],
    },
    {
        # Task cannot be scheduled — no specialist has the required skill.
        "description": "No matching skill — task is skipped",
        "fn": "assign_tasks",
        "args": [
            [{"specialist_id": "S1", "skills": {"java"}, "available": [[0, 100]]}],
            [{"task_id": "T1", "required_skill": "python", "duration": 10, "preferred_start": 0}],
        ],
        "expected": [],
    },
    {
        # Task duration exceeds all available intervals — cannot fit.
        "description": "Duration too long for available slots — task skipped",
        "fn": "assign_tasks",
        "args": [
            [{"specialist_id": "S1", "skills": {"python"}, "available": [[0, 10], [20, 25]]}],
            [{"task_id": "T1", "required_skill": "python", "duration": 15, "preferred_start": 0}],
        ],
        "expected": [],
    },
    {
        # preferred_start is beyond all available time — cannot schedule.
        "description": "preferred_start after all availability — task skipped",
        "fn": "assign_tasks",
        "args": [
            [{"specialist_id": "S1", "skills": {"python"}, "available": [[0, 50]]}],
            [{"task_id": "T1", "required_skill": "python", "duration": 10, "preferred_start": 60}],
        ],
        "expected": [],
    },
    {
        # Two specialists both qualify; pick the one offering the earlier start.
        # S1 available from [50,100], S2 available from [5,100].
        # Both have the skill. preferred_start=0.
        # S1 earliest start = 50, S2 earliest start = 5 → S2 wins.
        "description": "Two qualifying specialists — earliest start wins",
        "fn": "assign_tasks",
        "args": [
            [
                {"specialist_id": "S1", "skills": {"ml"}, "available": [[50, 100]]},
                {"specialist_id": "S2", "skills": {"ml"}, "available": [[5,  100]]},
            ],
            [{"task_id": "T1", "required_skill": "ml", "duration": 10, "preferred_start": 0}],
        ],
        "expected": [("T1", "S2", 5, 15)],
    },
    {
        # Tie-break: two specialists offer the same earliest start — pick lex smaller id.
        "description": "Tie on earliest start — lex smaller specialist_id wins",
        "fn": "assign_tasks",
        "args": [
            [
                {"specialist_id": "beta",  "skills": {"sql"}, "available": [[0, 100]]},
                {"specialist_id": "alpha", "skills": {"sql"}, "available": [[0, 100]]},
            ],
            [{"task_id": "T1", "required_skill": "sql", "duration": 20, "preferred_start": 0}],
        ],
        "expected": [("T1", "alpha", 0, 20)],
    },
    {
        # Three tasks, two specialists with different skills.
        # S1: python [0,100], S2: sql [0,100]
        # T1(python,dur=30,pref=0) → S1 [0,30]
        # T2(sql,   dur=20,pref=0) → S2 [0,20]
        # T3(python,dur=40,pref=0) → S1 remaining [30,100], start=30, end=70
        "description": "Three tasks, two specialists — parallel skill tracks",
        "fn": "assign_tasks",
        "args": [
            [
                {"specialist_id": "S1", "skills": {"python"}, "available": [[0, 100]]},
                {"specialist_id": "S2", "skills": {"sql"},    "available": [[0, 100]]},
            ],
            [
                {"task_id": "T1", "required_skill": "python", "duration": 30, "preferred_start": 0},
                {"task_id": "T2", "required_skill": "sql",    "duration": 20, "preferred_start": 0},
                {"task_id": "T3", "required_skill": "python", "duration": 40, "preferred_start": 0},
            ],
        ],
        # T1(pref=0) and T2(pref=0) tie → T1 < T2 lex → T1 first
        # T1 → S1 [0,30]. T2 → S2 [0,20]. T3 → S1 [30,70].
        "expected": [("T1", "S1", 0, 30), ("T2", "S2", 0, 20), ("T3", "S1", 30, 70)],
    },
]
