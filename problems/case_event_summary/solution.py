# ============================================================
# Problem: Case Event Summary Builder
# ============================================================
# You are given a list of event records for insurance cases.
#
# Each event is a dict with:
#   - case_id    (str)
#   - timestamp  (str, ISO 8601 — e.g. "2024-01-15T10:30:00")
#   - event_type (str)
#   - severity   (str — "low", "medium", or "high")
#
# Build a function that returns, for each case, a dict with:
#   - latest_event_type      (str)  — event_type of the most recent event
#   - high_severity_count    (int)  — total number of "high" severity events
#   - escalate               (bool) — True if the case should be escalated
#
# Escalation rules (either condition triggers escalation):
#   1. high_severity_count >= 3
#   2. latest_event_type == "legal_review"
#
# Return a dict mapping case_id -> summary dict.
#
# Example:
#   events = [
#       {"case_id": "A1", "timestamp": "2024-01-01T09:00:00", "event_type": "filed", "severity": "low"},
#       {"case_id": "A1", "timestamp": "2024-01-02T10:00:00", "event_type": "legal_review", "severity": "high"},
#   ]
#   Output: {
#       "A1": {
#           "latest_event_type": "legal_review",
#           "high_severity_count": 1,
#           "escalate": True,       # latest event is "legal_review"
#       }
#   }
# ============================================================
from collections import defaultdict


def build_case_summaries(events: list[dict]) -> dict[str, dict]:
    # Your solution here
    case_summary = {}

    # if we sort the events by event timestamp in descending order, we will get the latest event type
    sorted_events = sorted(events, key=lambda e: (-e["timestamp"], e["case_id"]))

    # need case id and severity counter in a dictionary
    case_severity_count = defaultdict(int)
    for event in sorted_events:
        case_id = event["case_id"]
        severity = event["severity"]

        if severity == "high":
            case_severity_count[case_id] += 1



    raise NotImplementedError
