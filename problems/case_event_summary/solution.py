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
from xmlrpc.client import Boolean


def build_case_summaries(events: list[dict]) -> dict[str, dict]:

    summary = {}

    # pass through all the events once to get severity counter and store the latest event
    for event in events:
        case_id = event["case_id"]

        if case_id not in summary:
            summary[case_id] = {
                "latest_timestamp": event["timestamp"],
                "latest_event_type": event["event_type"],
                "high_severity_count": 0
            }

        if event["timestamp"] > summary[case_id]["latest_timestamp"]:
            summary[case_id]["latest_timestamp"] = event["timestamp"]
            summary[case_id]["latest_event_type"] = event["event_type"]

        if event["severity"] == "high":
            summary[case_id]["high_severity_count"] += 1

    result = {}
    for case_id, data in summary.items():
        latest_event_type = data["latest_event_type"]
        high_count = data["high_severity_count"]
        escalated = high_count >= 3 or latest_event_type == "legal_review"

        result[case_id] = {
            "latest_event_type": latest_event_type,
            "high_severity_count": high_count,
            "escalate": escalated
        }

    return result
