# ============================================================
# Problem: Alert Deduplication Engine
# ============================================================
# A monitoring system emits alerts. Repeated alerts of the
# same type for the same tenant within 15 minutes should be
# collapsed into a single logical alert.
#
# Each alert is a dict with:
#   - tenant_id  (str)
#   - alert_type (str)
#   - timestamp  (int) — time in minutes from epoch
#
# Deduplication rule:
#   Process alerts in chronological order (sort by timestamp;
#   tie-break by tenant_id, then alert_type for determinism).
#   For each (tenant_id, alert_type) pair, track the timestamp
#   of the last emitted alert. A new alert is a duplicate if:
#
#       new_timestamp - last_emitted_timestamp <= 15
#
#   Duplicates are suppressed. When the gap exceeds 15 minutes,
#   the next alert starts a fresh window and is emitted.
#
# Return a tuple (deduplicated, suppressed_count) where:
#   - deduplicated (list[dict]): alerts that were emitted,
#     in chronological order, each dict preserving the original
#     tenant_id, alert_type, and timestamp fields.
#   - suppressed_count (int): number of alerts that were dropped.
#
# Example:
#   alerts = [
#       {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 0},
#       {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 10},  # dup (gap=10)
#       {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 20},  # new (gap=20)
#   ]
#   Output: (
#       [
#           {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 0},
#           {"tenant_id": "A", "alert_type": "cpu_high", "timestamp": 20},
#       ],
#       1
#   )
# ============================================================
from collections import defaultdict
from collections import deque


def deduplicate_alerts(alerts: list[dict]) -> tuple[list[dict], int]:

    # result set containing dedup alerts
    result = []

    # keeping count of alerts dropped
    dropped_alerts = []

    # sort the alerts by timestamp, tenant_id and then alert_type
    sorted_alerts = sorted(alerts, key=lambda a: (a["timestamp"],a["tenant_id"],a["alert_type"]))

    # tuple(tenant_id, alert_type) -> latest timestamp
    last_emitted = defaultdict(int)

    # go over the alerts one by one
    for alert in sorted_alerts:
        tenant_id = alert["tenant_id"]
        alert_type = alert["alert_type"]
        timestamp = alert["timestamp"]

        if (tenant_id, alert_type) not in last_emitted:
            last_emitted[(tenant_id, alert_type)] = timestamp
            result.append(alert)
        else:
            # if we have seen this alert before, check the dedup rule
            if timestamp - last_emitted[(tenant_id, alert_type)] <= 15:
                # means it's a duplicate and needs to be dropped, increase drop count
                dropped_alerts.append(alert)
            else:
                # update the latest timestamp of the existing combination
                last_emitted[(tenant_id, alert_type)] = timestamp
                result.append(alert)


    return result, len(dropped_alerts)
