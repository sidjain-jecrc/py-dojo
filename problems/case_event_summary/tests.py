TEST_CASES = [
    {
        # Single case, two events. Latest is "legal_review" → escalate.
        # Only one high-severity event (not enough alone, but legal_review triggers it).
        "description": "Single case — escalate due to legal_review latest event",
        "fn": "build_case_summaries",
        "args": [[
            {"case_id": "A1", "timestamp": "2024-01-01T09:00:00", "event_type": "filed",        "severity": "low"},
            {"case_id": "A1", "timestamp": "2024-01-02T10:00:00", "event_type": "legal_review", "severity": "high"},
        ]],
        "expected": {
            "A1": {"latest_event_type": "legal_review", "high_severity_count": 1, "escalate": True},
        },
    },
    {
        # Single case with 3 high-severity events. Latest is NOT legal_review,
        # but count alone triggers escalation.
        "description": "Single case — escalate due to 3 high-severity events",
        "fn": "build_case_summaries",
        "args": [[
            {"case_id": "B1", "timestamp": "2024-02-01T08:00:00", "event_type": "inspection",  "severity": "high"},
            {"case_id": "B1", "timestamp": "2024-02-02T09:00:00", "event_type": "dispute",     "severity": "high"},
            {"case_id": "B1", "timestamp": "2024-02-03T10:00:00", "event_type": "appeal",      "severity": "high"},
        ]],
        "expected": {
            "B1": {"latest_event_type": "appeal", "high_severity_count": 3, "escalate": True},
        },
    },
    {
        # Single case — 2 high-severity events, latest is not legal_review.
        # Neither escalation condition is met.
        "description": "Single case — no escalation (2 high events, no legal_review)",
        "fn": "build_case_summaries",
        "args": [[
            {"case_id": "C1", "timestamp": "2024-03-01T07:00:00", "event_type": "filed",       "severity": "high"},
            {"case_id": "C1", "timestamp": "2024-03-02T08:00:00", "event_type": "inspection",  "severity": "high"},
            {"case_id": "C1", "timestamp": "2024-03-03T09:00:00", "event_type": "closed",      "severity": "low"},
        ]],
        "expected": {
            "C1": {"latest_event_type": "closed", "high_severity_count": 2, "escalate": False},
        },
    },
    {
        # Multiple cases in a single event list. Each case is independent.
        # Case D1: 1 high event, latest is "closed"       → no escalation
        # Case D2: 0 high events, latest is "legal_review" → escalate
        "description": "Multiple cases — mixed escalation outcomes",
        "fn": "build_case_summaries",
        "args": [[
            {"case_id": "D1", "timestamp": "2024-04-01T10:00:00", "event_type": "filed",        "severity": "low"},
            {"case_id": "D1", "timestamp": "2024-04-02T11:00:00", "event_type": "dispute",      "severity": "high"},
            {"case_id": "D1", "timestamp": "2024-04-03T12:00:00", "event_type": "closed",       "severity": "low"},
            {"case_id": "D2", "timestamp": "2024-04-01T09:00:00", "event_type": "filed",        "severity": "low"},
            {"case_id": "D2", "timestamp": "2024-04-04T14:00:00", "event_type": "legal_review", "severity": "medium"},
        ]],
        "expected": {
            "D1": {"latest_event_type": "closed",       "high_severity_count": 1, "escalate": False},
            "D2": {"latest_event_type": "legal_review", "high_severity_count": 0, "escalate": True},
        },
    },
    {
        # Events arrive out of chronological order. The function must use
        # timestamps to determine the latest event, not list position.
        "description": "Events out of order — latest determined by timestamp",
        "fn": "build_case_summaries",
        "args": [[
            {"case_id": "E1", "timestamp": "2024-05-03T15:00:00", "event_type": "appeal",      "severity": "low"},
            {"case_id": "E1", "timestamp": "2024-05-01T08:00:00", "event_type": "legal_review", "severity": "high"},
            {"case_id": "E1", "timestamp": "2024-05-02T12:00:00", "event_type": "inspection",  "severity": "high"},
        ]],
        "expected": {
            "E1": {"latest_event_type": "appeal", "high_severity_count": 2, "escalate": False},
        },
    },
    {
        # Both escalation conditions are true simultaneously.
        # legal_review is the latest event AND there are 3+ high-severity events.
        "description": "Both escalation conditions true at once",
        "fn": "build_case_summaries",
        "args": [[
            {"case_id": "F1", "timestamp": "2024-06-01T08:00:00", "event_type": "filed",        "severity": "high"},
            {"case_id": "F1", "timestamp": "2024-06-02T09:00:00", "event_type": "dispute",      "severity": "high"},
            {"case_id": "F1", "timestamp": "2024-06-03T10:00:00", "event_type": "appeal",       "severity": "high"},
            {"case_id": "F1", "timestamp": "2024-06-04T11:00:00", "event_type": "legal_review", "severity": "high"},
        ]],
        "expected": {
            "F1": {"latest_event_type": "legal_review", "high_severity_count": 4, "escalate": True},
        },
    },
    {
        # Single event per case, severity is not high, event is not legal_review.
        "description": "Single low-severity event — no escalation",
        "fn": "build_case_summaries",
        "args": [[
            {"case_id": "G1", "timestamp": "2024-07-01T10:00:00", "event_type": "filed", "severity": "low"},
        ]],
        "expected": {
            "G1": {"latest_event_type": "filed", "high_severity_count": 0, "escalate": False},
        },
    },
]
