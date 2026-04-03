HINT = {
    "approach": "Min-heap (priority queue) over specialists",
    "time_complexity": "O(n log k)  — n claims, k specialists",
    "space_complexity": "O(k)",
    "reasoning": """
Maintain a min-heap keyed on (current_load, specialist_id).
For each claim, pop the eligible specialist with the lowest
load in O(log k), assign the claim, update their load, and
push them back.

A naive approach scans all specialists for every claim —
O(n × k). The heap reduces each assignment to O(log k),
giving O(n log k) overall.

If skills filtering is needed, pre-build a map from each
skill to the list of specialists who have it, so you only
heapify the eligible subset rather than all specialists.
""",
}
