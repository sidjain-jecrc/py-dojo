HINT = {
    "approach": "Per-tenant sort + two-pointer sliding window",
    "time_complexity": "O(n log n)  — dominated by sorting per tenant",
    "space_complexity": "O(n)",
    "reasoning": """
Group events by tenant_id, then for each tenant sort their
events by timestamp. Use two pointers (left, right): advance
right one event at a time, adding units_used to a running sum.
While the window [left, right] spans more than 59 minutes,
subtract events[left].units_used and advance left.
If the running sum ever exceeds the threshold, flag the tenant.

This is O(n log n) due to sorting and O(n) for the sweep —
far better than the O(n²) approach of re-summing the window
from scratch for every new event.

A deque works equally well as the two-pointer and may feel
more natural if you think of the window as a sliding queue.
""",
}
