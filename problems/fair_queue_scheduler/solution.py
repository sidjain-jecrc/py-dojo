# ============================================================
# Problem: Fair Queue Scheduler
# ============================================================
# A platform serves jobs from multiple client tenants.
# The scheduler must be fair — no tenant should monopolize
# the system — while still preferring older work.
#
# Each job is a dict with:
#   - tenant_id  (str)
#   - job_id     (str)
#   - created_at (int) — submission time in seconds from epoch
#
# Scheduling rules:
#   1. Jobs are processed in rounds.
#   2. Each round, every tenant with pending jobs gets exactly
#      one slot (preventing monopolization).
#   3. Within a round, slots are ordered by the created_at of
#      each tenant's oldest pending job — oldest goes first.
#   4. Tie-break: if two tenants have the same oldest created_at,
#      order them lexicographically by tenant_id.
#   5. Within a tenant's own queue, jobs are processed oldest-first.
#
# Return the list of job_ids in the order they are processed.
#
# Example:
#   jobs = [
#       {"tenant_id": "A", "job_id": "A1", "created_at": 1},
#       {"tenant_id": "A", "job_id": "A2", "created_at": 5},
#       {"tenant_id": "B", "job_id": "B1", "created_at": 2},
#       {"tenant_id": "C", "job_id": "C1", "created_at": 3},
#   ]
#
#   Round 1 — one slot per active tenant, ordered by oldest head:
#     A head=1, B head=2, C head=3  →  A1, B1, C1
#   Round 2 — only A and B remain:
#     A head=5, B exhausted after B1  →  wait, B is done
#     Only A remains  →  A2
#
#   Output: ["A1", "B1", "C1", "A2"]
# ============================================================


def schedule_jobs(jobs: list[dict]) -> list[str]:
    # Your solution here
    raise NotImplementedError
