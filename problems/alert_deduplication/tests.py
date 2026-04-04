TEST_CASES = [
    {
        # No repeated (tenant, type) pair — all alerts pass through.
        "description": "No duplicates — all alerts emitted",
        "fn": "deduplicate_alerts",
        "args": [[
            {"tenant_id": "A", "alert_type": "cpu_high",  "timestamp": 0},
            {"tenant_id": "A", "alert_type": "disk_full",  "timestamp": 5},
            {"tenant_id": "B", "alert_type": "cpu_high",  "timestamp": 10},
        ]],
        "expected": (
            [
                {"tenant_id": "A", "alert_type": "cpu_high",  "timestamp": 0},
                {"tenant_id": "A", "alert_type": "disk_full", "timestamp": 5},
                {"tenant_id": "B", "alert_type": "cpu_high",  "timestamp": 10},
            ],
            0,
        ),
    },
    {
        # Three alerts, same tenant+type, all within 15 min of the first.
        # Only the first is emitted; the other two are suppressed.
        "description": "Three identical alerts within window — only first emitted",
        "fn": "deduplicate_alerts",
        "args": [[
            {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 0},
            {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 7},
            {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 14},
        ]],
        "expected": (
            [{"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 0}],
            2,
        ),
    },
    {
        # Gap between 1st and 3rd alert is 20 minutes (> 15).
        # The 2nd alert (t=10) is a duplicate of t=0 (gap=10 ≤ 15).
        # The 3rd alert (t=20) is a new window (gap=20-0=20 > 15 from last emitted t=0).
        "description": "Alert resets window after gap > 15 — two windows",
        "fn": "deduplicate_alerts",
        "args": [[
            {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 0},
            {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 10},
            {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 20},
        ]],
        "expected": (
            [
                {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 0},
                {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 20},
            ],
            1,
        ),
    },
    {
        # Boundary: gap of exactly 15 minutes → still a duplicate (≤ 15).
        "description": "Gap exactly 15 minutes — still a duplicate",
        "fn": "deduplicate_alerts",
        "args": [[
            {"tenant_id": "T1", "alert_type": "mem_low", "timestamp": 100},
            {"tenant_id": "T1", "alert_type": "mem_low", "timestamp": 115},
        ]],
        "expected": (
            [{"tenant_id": "T1", "alert_type": "mem_low", "timestamp": 100}],
            1,
        ),
    },
    {
        # Boundary: gap of 16 minutes → new alert (> 15).
        "description": "Gap of 16 minutes — new alert emitted",
        "fn": "deduplicate_alerts",
        "args": [[
            {"tenant_id": "T1", "alert_type": "mem_low", "timestamp": 100},
            {"tenant_id": "T1", "alert_type": "mem_low", "timestamp": 116},
        ]],
        "expected": (
            [
                {"tenant_id": "T1", "alert_type": "mem_low", "timestamp": 100},
                {"tenant_id": "T1", "alert_type": "mem_low", "timestamp": 116},
            ],
            0,
        ),
    },
    {
        # Deduplication is per (tenant_id, alert_type) pair.
        # Same alert_type for different tenants are independent.
        # Same tenant with different alert_types are independent.
        "description": "Deduplication scoped to (tenant, type) — different pairs independent",
        "fn": "deduplicate_alerts",
        "args": [[
            {"tenant_id": "A", "alert_type": "cpu_high",  "timestamp": 0},
            {"tenant_id": "B", "alert_type": "cpu_high",  "timestamp": 5},   # different tenant
            {"tenant_id": "A", "alert_type": "disk_full", "timestamp": 8},   # different type
            {"tenant_id": "A", "alert_type": "cpu_high",  "timestamp": 10},  # dup of A/cpu at t=0
        ]],
        "expected": (
            [
                {"tenant_id": "A", "alert_type": "cpu_high",  "timestamp": 0},
                {"tenant_id": "B", "alert_type": "cpu_high",  "timestamp": 5},
                {"tenant_id": "A", "alert_type": "disk_full", "timestamp": 8},
            ],
            1,
        ),
    },
    {
        # Input arrives out of timestamp order — must sort before processing.
        # After sorting: t=0, t=5(dup), t=20(new window).
        "description": "Out-of-order input — sorted before deduplication",
        "fn": "deduplicate_alerts",
        "args": [[
            {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 20},
            {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 0},
            {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 5},
        ]],
        "expected": (
            [
                {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 0},
                {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 20},
            ],
            1,
        ),
    },
    {
        # Long sequence: three distinct windows for one (tenant, type) pair.
        # t=0 → emitted.  t=10 → dup (gap 10).  t=14 → dup (gap 14 from t=0).
        # t=16 → new window (gap 16 from t=0). t=30 → dup (gap 14 from t=16).
        # t=33 → new window (gap 17 from t=16).
        "description": "Three windows for one pair — interleaved emits and suppression",
        "fn": "deduplicate_alerts",
        "args": [[
            {"tenant_id": "X", "alert_type": "err", "timestamp": 0},
            {"tenant_id": "X", "alert_type": "err", "timestamp": 10},
            {"tenant_id": "X", "alert_type": "err", "timestamp": 14},
            {"tenant_id": "X", "alert_type": "err", "timestamp": 16},
            {"tenant_id": "X", "alert_type": "err", "timestamp": 30},
            {"tenant_id": "X", "alert_type": "err", "timestamp": 33},
        ]],
        "expected": (
            [
                {"tenant_id": "X", "alert_type": "err", "timestamp": 0},
                {"tenant_id": "X", "alert_type": "err", "timestamp": 16},
                {"tenant_id": "X", "alert_type": "err", "timestamp": 33},
            ],
            3,
        ),
    },
    {
        # Empty input — nothing to emit, nothing suppressed.
        "description": "Empty alert list",
        "fn": "deduplicate_alerts",
        "args": [[]],
        "expected": ([], 0),
    },
    {
        # Single alert — always emitted.
        "description": "Single alert — emitted with 0 suppressed",
        "fn": "deduplicate_alerts",
        "args": [[
            {"tenant_id": "T1", "alert_type": "timeout", "timestamp": 42},
        ]],
        "expected": (
            [{"tenant_id": "T1", "alert_type": "timeout", "timestamp": 42}],
            0,
        ),
    },
]
