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
from collections import deque, defaultdict


def find_flagged_tenants(events: list[dict], threshold: int) -> list[str]:

    flagged_tenants = set()
    tenant_window_sum = defaultdict(int)

    sorted_events = sorted(events, key=lambda e: (e["tenant_id"], e["timestamp"]))
    tenant_window = defaultdict(deque)  # deque of (timestamp, units_used)

    for event in sorted_events:
        tenant_id = event["tenant_id"]
        now = event["timestamp"]

        # evict events that have fallen outside the 60-minute window
        while tenant_window[tenant_id] and tenant_window[tenant_id][0][0] <= now - 60:
            _, old_units = tenant_window[tenant_id].popleft()
            tenant_window_sum[tenant_id] -= old_units

        tenant_window_sum[tenant_id] += event["units_used"]
        tenant_window[tenant_id].append((now, event["units_used"]))

        if tenant_window_sum[tenant_id] > threshold:
            flagged_tenants.add(tenant_id)

    return sorted(flagged_tenants)
