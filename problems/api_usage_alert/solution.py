# ============================================================
# Problem: Tenant API Usage Alert
# ============================================================
# You are given a stream of API usage events and a usage
# threshold. Flag any tenant whose usage spikes within a
# rolling window.
#
# Input:
#   - events:    list of dicts, each with:
#       - "tenant_id"  (str)
#       - "timestamp"  (int) — time in minutes from epoch
#       - "units_used" (int) — API units consumed in this event
#   - threshold: (int) — maximum allowed units in any 60-minute window
#
# A tenant is flagged if there exists any 60-minute window
# [t, t + 59] (inclusive on both ends) in which their total
# units_used exceeds the threshold.
#
# Return a sorted list of flagged tenant_ids.
# An empty list means no tenants were flagged.
#
# Example:
#   events = [
#       {"tenant_id": "A", "timestamp": 0,  "units_used": 60},
#       {"tenant_id": "A", "timestamp": 30, "units_used": 50},  # window [0,59]: 60+50=110
#       {"tenant_id": "B", "timestamp": 0,  "units_used": 40},
#       {"tenant_id": "B", "timestamp": 70, "units_used": 70},  # no window contains both
#   ]
#   threshold = 100
#   Output: ["A"]   # B never exceeds 100 in any single 60-min window
#
# Notes:
#   - Events may arrive out of timestamp order.
#   - A tenant may appear many times across events.
#   - If no tenant is flagged, return [].
# ============================================================


def find_flagged_tenants(events: list[dict], threshold: int) -> list[str]:
    # Your solution here
    raise NotImplementedError
