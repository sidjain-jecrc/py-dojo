# ============================================================
# Problem: Specialist Availability Matching
# ============================================================
# Assign tasks to specialists respecting skill requirements,
# time availability, and fairness across tasks.
#
# Each specialist is a dict with:
#   - specialist_id (str)
#   - skills        (set of str)
#   - available     (list of [start, end] intervals, integers,
#                    non-overlapping and sorted)
#
# Each task is a dict with:
#   - task_id         (str)
#   - required_skill  (str)
#   - duration        (int) — units of time needed
#   - preferred_start (int) — earliest acceptable start time
#
# Assignment rules:
#   1. The specialist must have the required skill.
#   2. The assigned slot must fit entirely within one of the
#      specialist's available intervals.
#   3. The assigned start >= preferred_start.
#   4. Tasks are considered in ascending preferred_start order
#      (ties broken by task_id lexicographically).
#   5. For each task, among all valid (specialist, slot) options,
#      choose the one with the earliest assigned_start.
#      Tie-break by specialist_id lexicographically.
#   6. Once a slot is used, that time range is removed from the
#      specialist's availability for future tasks.
#   7. Tasks that cannot be assigned to any specialist are skipped.
#
# Return a list of tuples:
#   (task_id, specialist_id, assigned_start, assigned_end)
# in the order tasks were assigned (i.e. sorted by assigned_start,
# then task_id).
#
# Example:
#   specialists = [
#       {"specialist_id": "S1", "skills": {"python"},
#        "available": [[0, 100]]},
#   ]
#   tasks = [
#       {"task_id": "T1", "required_skill": "python",
#        "duration": 30, "preferred_start": 10},
#   ]
#   Output: [("T1", "S1", 10, 40)]
#     S1 is available [0,100]; preferred_start=10; 10+30=40 ≤ 100 ✓
# ============================================================


def assign_tasks(
    specialists: list[dict],
    tasks: list[dict],
) -> list[tuple[str, str, int, int]]:
    # Your solution here
    raise NotImplementedError
