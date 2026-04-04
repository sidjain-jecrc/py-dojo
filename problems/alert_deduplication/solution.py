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


def deduplicate_alerts(alerts: list[dict]) -> tuple[list[dict], int]:
    # Your solution here
    raise NotImplementedError
