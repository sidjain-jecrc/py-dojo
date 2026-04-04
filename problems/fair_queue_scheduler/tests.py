TEST_CASES = [
    {
        # Single tenant — output is just that tenant's jobs oldest-first.
        "description": "Single tenant — jobs in created_at order",
        "fn": "schedule_jobs",
        "args": [[
            {"tenant_id": "A", "job_id": "A1", "created_at": 10},
            {"tenant_id": "A", "job_id": "A2", "created_at": 5},
            {"tenant_id": "A", "job_id": "A3", "created_at": 20},
        ]],
        "expected": ["A2", "A1", "A3"],
    },
    {
        # Two tenants, equal depth.
        # Round 1: A head=1, B head=2  → A1, B1
        # Round 2: A head=5, B head=6  → A2, B2
        "description": "Two tenants, equal depth — interleaved by round",
        "fn": "schedule_jobs",
        "args": [[
            {"tenant_id": "A", "job_id": "A1", "created_at": 1},
            {"tenant_id": "A", "job_id": "A2", "created_at": 5},
            {"tenant_id": "B", "job_id": "B1", "created_at": 2},
            {"tenant_id": "B", "job_id": "B2", "created_at": 6},
        ]],
        "expected": ["A1", "B1", "A2", "B2"],
    },
    {
        # Tenant A has 3 jobs, B has 1.
        # Round 1: A head=1, B head=2  → A1, B1
        # Round 2: only A remains      → A2
        # Round 3: only A remains      → A3
        "description": "Unequal depths — shorter tenant exhausted early",
        "fn": "schedule_jobs",
        "args": [[
            {"tenant_id": "A", "job_id": "A1", "created_at": 1},
            {"tenant_id": "A", "job_id": "A2", "created_at": 3},
            {"tenant_id": "A", "job_id": "A3", "created_at": 7},
            {"tenant_id": "B", "job_id": "B1", "created_at": 2},
        ]],
        "expected": ["A1", "B1", "A2", "A3"],
    },
    {
        # Three tenants. Tenant C has only one job.
        # Round 1: A head=1, B head=2, C head=3  → A1, B1, C1
        # Round 2: A head=5, B head=10            → A2, B2
        "description": "Three tenants — one exhausted after round 1",
        "fn": "schedule_jobs",
        "args": [[
            {"tenant_id": "A", "job_id": "A1", "created_at": 1},
            {"tenant_id": "A", "job_id": "A2", "created_at": 5},
            {"tenant_id": "B", "job_id": "B1", "created_at": 2},
            {"tenant_id": "B", "job_id": "B2", "created_at": 10},
            {"tenant_id": "C", "job_id": "C1", "created_at": 3},
        ]],
        "expected": ["A1", "B1", "C1", "A2", "B2"],
    },
    {
        # Within a round, two tenants have the same oldest created_at.
        # Tie-break lexicographically by tenant_id: "alpha" < "beta".
        "description": "Same created_at in a round — tie-break by tenant_id",
        "fn": "schedule_jobs",
        "args": [[
            {"tenant_id": "beta",  "job_id": "B1", "created_at": 10},
            {"tenant_id": "alpha", "job_id": "A1", "created_at": 10},
        ]],
        "expected": ["A1", "B1"],
    },
    {
        # Jobs arrive out of created_at order within a tenant's list.
        # The scheduler must still process each tenant's jobs oldest-first.
        # Round 1: A head=2, B head=1  → B1, A1   (B's head is older)
        # Round 2: A head=5, B head=8  → A2, B2
        "description": "Jobs submitted out of order — oldest head wins each round",
        "fn": "schedule_jobs",
        "args": [[
            {"tenant_id": "A", "job_id": "A1", "created_at": 2},
            {"tenant_id": "A", "job_id": "A2", "created_at": 5},
            {"tenant_id": "B", "job_id": "B1", "created_at": 1},
            {"tenant_id": "B", "job_id": "B2", "created_at": 8},
        ]],
        "expected": ["B1", "A1", "A2", "B2"],
    },
    {
        # One tenant with many jobs, another with one very old job.
        # The old job should come first in round 1, then the deep tenant runs alone.
        # Round 1: A head=100, B head=1  → B1, A1
        # Round 2–4: only A remains      → A2, A3, A4
        "description": "One very old job from small tenant — goes first in round 1",
        "fn": "schedule_jobs",
        "args": [[
            {"tenant_id": "A", "job_id": "A1", "created_at": 100},
            {"tenant_id": "A", "job_id": "A2", "created_at": 200},
            {"tenant_id": "A", "job_id": "A3", "created_at": 300},
            {"tenant_id": "A", "job_id": "A4", "created_at": 400},
            {"tenant_id": "B", "job_id": "B1", "created_at": 1},
        ]],
        "expected": ["B1", "A1", "A2", "A3", "A4"],
    },
    {
        # Single job — trivial.
        "description": "Single job — returned immediately",
        "fn": "schedule_jobs",
        "args": [[
            {"tenant_id": "solo", "job_id": "J1", "created_at": 42},
        ]],
        "expected": ["J1"],
    },
    {
        # Four tenants, each with two jobs.
        # Round 1 order by head: D(1) < C(2) < B(3) < A(4)  → D1, C1, B1, A1
        # Round 2 order by head: D(5) < C(6) < B(7) < A(8)  → D2, C2, B2, A2
        "description": "Four tenants, two jobs each — two full rounds",
        "fn": "schedule_jobs",
        "args": [[
            {"tenant_id": "A", "job_id": "A1", "created_at": 4},
            {"tenant_id": "A", "job_id": "A2", "created_at": 8},
            {"tenant_id": "B", "job_id": "B1", "created_at": 3},
            {"tenant_id": "B", "job_id": "B2", "created_at": 7},
            {"tenant_id": "C", "job_id": "C1", "created_at": 2},
            {"tenant_id": "C", "job_id": "C2", "created_at": 6},
            {"tenant_id": "D", "job_id": "D1", "created_at": 1},
            {"tenant_id": "D", "job_id": "D2", "created_at": 5},
        ]],
        "expected": ["D1", "C1", "B1", "A1", "D2", "C2", "B2", "A2"],
    },
]
