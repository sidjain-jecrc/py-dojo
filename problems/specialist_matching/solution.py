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

    result_set = []
    tasks.sort(key=lambda x: (x["preferred_start"], x["task_id"]))

    for task in tasks:
        required_skill = task["required_skill"]
        duration = task["duration"]
        preferred_start = task["preferred_start"]

        # (specialist_id, candidate_start, candidate_end, original_slot)
        eligible_specialists = []
        for specialist in specialists:
            if required_skill in specialist["skills"]:
                for slot in specialist["available"]:
                    candidate_start = max(preferred_start, slot[0])
                    candidate_end = candidate_start + duration
                    if candidate_end <= slot[1]:
                        eligible_specialists.append((specialist["specialist_id"], candidate_start, candidate_end, slot))
                        break  # slots are sorted; first valid slot is earliest

        if not eligible_specialists:
            continue

        eligible_specialists.sort(key=lambda x: (x[1], x[0]))
        winner_id, assigned_start, assigned_end, used_slot = eligible_specialists[0]

        # Split the used slot, discarding zero-length fragments
        winner = next(sp for sp in specialists if sp["specialist_id"] == winner_id)
        new_slots = []
        for s in winner["available"]:
            if s == used_slot:
                if used_slot[0] < assigned_start:
                    new_slots.append([used_slot[0], assigned_start])
                if assigned_end < used_slot[1]:
                    new_slots.append([assigned_end, used_slot[1]])
            else:
                new_slots.append(s)
        winner["available"] = new_slots

        result_set.append((task["task_id"], winner_id, assigned_start, assigned_end))

    result_set.sort(key=lambda x: (x[2], x[0]))
    return result_set
