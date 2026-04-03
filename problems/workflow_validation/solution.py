# ============================================================
# Problem: Workflow Dependency Validation
# ============================================================
# A claims workflow consists of tasks, where some tasks must
# be completed before others can begin.
#
# Input:
#   - tasks:        list of task name strings
#   - dependencies: list of (task, prerequisite_task) tuples,
#                   meaning prerequisite_task must finish before task
#
# ---
# Part 1 — validate_workflow
# ---
# Return True if all tasks can be completed (no circular
# dependencies), False otherwise.
#
# Example — feasible:
#   tasks        = ["intake", "review", "approve", "close"]
#   dependencies = [("review","intake"),("approve","review"),("close","approve")]
#   Output: True
#
# Example — infeasible (A waits on B, B waits on A):
#   tasks        = ["A", "B", "C"]
#   dependencies = [("B","A"), ("A","B"), ("C","A")]
#   Output: False
#
# ---
# Part 2 (bonus) — execution_order
# ---
# Return one valid execution order as a list if feasible,
# or None if the workflow contains a cycle.
#
# Notes:
#   - Any valid topological order is accepted.
#   - All tasks in dependencies are guaranteed to appear in tasks.
# ============================================================


def validate_workflow(
    tasks: list[str],
    dependencies: list[tuple[str, str]],
) -> bool:
    # Your solution here
    raise NotImplementedError


def execution_order(
    tasks: list[str],
    dependencies: list[tuple[str, str]],
) -> list[str] | None:
    # Your solution here (bonus)
    raise NotImplementedError
