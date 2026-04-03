TEST_CASES = [
    {
        # Two events for tenant A, 30 minutes apart — both inside a 60-min window.
        # Combined usage 110 > 100 → flagged.
        # Tenant B never exceeds threshold in any single window.
        "description": "One tenant flagged, one safe — basic sliding window",
        "fn": "find_flagged_tenants",
        "args": [
            [
                {"tenant_id": "A", "timestamp": 0,  "units_used": 60},
                {"tenant_id": "A", "timestamp": 30, "units_used": 50},
                {"tenant_id": "B", "timestamp": 0,  "units_used": 40},
                {"tenant_id": "B", "timestamp": 70, "units_used": 70},
            ],
            100,
        ],
        "expected": ["A"],
    },
    {
        # Total usage exactly equals threshold — should NOT be flagged
        # (rule is strictly greater than).
        "description": "Usage exactly at threshold — not flagged",
        "fn": "find_flagged_tenants",
        "args": [
            [
                {"tenant_id": "T1", "timestamp": 0,  "units_used": 50},
                {"tenant_id": "T1", "timestamp": 59, "units_used": 50},
            ],
            100,
        ],
        "expected": [],
    },
    {
        # Usage one unit over threshold — flagged.
        "description": "Usage one unit over threshold — flagged",
        "fn": "find_flagged_tenants",
        "args": [
            [
                {"tenant_id": "T1", "timestamp": 0,  "units_used": 50},
                {"tenant_id": "T1", "timestamp": 59, "units_used": 51},
            ],
            100,
        ],
        "expected": ["T1"],
    },
    {
        # Events exactly 60 minutes apart sit in different windows
        # ([0,59] and [60,119]) — they never overlap, so usage per window
        # is only 70 each, below threshold.
        "description": "Events 60 minutes apart — fall in separate windows, not flagged",
        "fn": "find_flagged_tenants",
        "args": [
            [
                {"tenant_id": "T1", "timestamp": 0,  "units_used": 70},
                {"tenant_id": "T1", "timestamp": 60, "units_used": 70},
            ],
            100,
        ],
        "expected": [],
    },
    {
        # Events arrive out of timestamp order — function must sort before windowing.
        "description": "Out-of-order events — still detected correctly",
        "fn": "find_flagged_tenants",
        "args": [
            [
                {"tenant_id": "A", "timestamp": 55, "units_used": 80},
                {"tenant_id": "A", "timestamp": 10, "units_used": 80},
            ],
            100,
        ],
        "expected": ["A"],
    },
    {
        # Many small events; no single 60-min window accumulates enough.
        # Each burst of 3 events (30 units total) is 70 minutes apart from the next,
        # so consecutive bursts never share a window.
        "description": "Spread-out small bursts — never exceeds threshold in any window",
        "fn": "find_flagged_tenants",
        "args": [
            [
                {"tenant_id": "T1", "timestamp": 0,   "units_used": 10},
                {"tenant_id": "T1", "timestamp": 10,  "units_used": 10},
                {"tenant_id": "T1", "timestamp": 20,  "units_used": 10},
                {"tenant_id": "T1", "timestamp": 90,  "units_used": 10},
                {"tenant_id": "T1", "timestamp": 100, "units_used": 10},
                {"tenant_id": "T1", "timestamp": 110, "units_used": 10},
            ],
            50,
        ],
        "expected": [],
    },
    {
        # Multiple tenants; result must be sorted alphabetically.
        "description": "Multiple flagged tenants — result is sorted",
        "fn": "find_flagged_tenants",
        "args": [
            [
                {"tenant_id": "charlie", "timestamp": 0,  "units_used": 200},
                {"tenant_id": "alice",   "timestamp": 0,  "units_used": 200},
                {"tenant_id": "bob",     "timestamp": 0,  "units_used": 50},
            ],
            100,
        ],
        "expected": ["alice", "charlie"],
    },
    {
        # The spike comes from a third event that slides into range of the first.
        # Event timestamps: 0, 40, 58 — all within [0, 59].
        # Window sum = 40 + 35 + 40 = 115 > 100.
        "description": "Three-event window — cumulative spike detected",
        "fn": "find_flagged_tenants",
        "args": [
            [
                {"tenant_id": "X", "timestamp": 0,  "units_used": 40},
                {"tenant_id": "X", "timestamp": 40, "units_used": 35},
                {"tenant_id": "X", "timestamp": 58, "units_used": 40},
            ],
            100,
        ],
        "expected": ["X"],
    },
    {
        # Tenant has high total usage overall but each 60-min window is fine.
        # Events: 80 at t=0, 80 at t=61, 80 at t=122 — consecutive events are
        # always 61 minutes apart, so each window holds at most one event.
        "description": "High total usage but never a spike — not flagged",
        "fn": "find_flagged_tenants",
        "args": [
            [
                {"tenant_id": "T1", "timestamp": 0,   "units_used": 80},
                {"tenant_id": "T1", "timestamp": 61,  "units_used": 80},
                {"tenant_id": "T1", "timestamp": 122, "units_used": 80},
            ],
            100,
        ],
        "expected": [],
    },
    {
        # No events at all — nothing to flag.
        "description": "Empty event list — no flagged tenants",
        "fn": "find_flagged_tenants",
        "args": [[], 100],
        "expected": [],
    },
    {
        # Single event exceeds threshold by itself.
        "description": "Single event exceeds threshold alone",
        "fn": "find_flagged_tenants",
        "args": [
            [{"tenant_id": "T1", "timestamp": 0, "units_used": 150}],
            100,
        ],
        "expected": ["T1"],
    },
]
