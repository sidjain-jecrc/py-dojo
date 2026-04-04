HINT = {
    "approach": "Min-heap per round over tenant head jobs",
    "time_complexity": "O(n log k)  — n total jobs, k active tenants",
    "space_complexity": "O(n)",
    "reasoning": """
Pre-sort each tenant's job queue by created_at (O(n log n) once).
Then maintain a min-heap of (head_created_at, tenant_id, job_deque),
one entry per tenant.

Each round: pop ALL entries from the heap — these are this round's
active tenants, already in oldest-head order thanks to the heap
property. Take one job from each deque, emit it, then push the
tenant back if it still has jobs.

Popping k entries per round costs O(k log k). Summed over all
rounds this is O(n log k) — each of the n jobs triggers at most
one heap push and one pop.

The naive approach (re-scan all tenants each round to find the
oldest head) is O(n × k). The heap eliminates that scan.
""",
}
