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
from collections import defaultdict, deque


def validate_workflow(
    tasks: list[str],
    dependencies: list[tuple[str, str]],
) -> bool:

    # initialize in degree first based on tasks
    in_degree = {u:0 for u in tasks}

    # build a graph using dictionary of lists
    adjacency_list = defaultdict(list)

    # populate the graph
    for dependency in dependencies:
        adjacency_list[dependency[1]].append(dependency[0])
        in_degree[dependency[0]] += 1

    # add nodes with in_degree 0 to the queue
    queue = deque([u for u in tasks if in_degree[u]==0])

    order = []
    # after taking out one task, add depending tasks to the queue
    while queue:
        current_task = queue.popleft()
        order.append(current_task)

        for neighbor in adjacency_list[current_task]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.appendleft(neighbor)


    return len(order) == len(tasks)

def execution_order(
    tasks: list[str],
    dependencies: list[tuple[str, str]],
) -> list[str] | None:

    # initialize in degree first based on tasks
    in_degree = {u:0 for u in tasks}

    # build a graph using dictionary of lists
    adjacency_list = defaultdict(list)

    # populate the graph
    for dependency in dependencies:
        adjacency_list[dependency[1]].append(dependency[0])
        in_degree[dependency[0]] += 1

    # add nodes with in_degree 0 to the queue
    queue = deque()
    for t in tasks:
        if in_degree[t] == 0:
            queue.append(t)

    order = []
    # after taking out one task, add depending tasks to the queue
    while queue:
        current_task = queue.popleft()
        order.append(current_task)

        for neighbor in adjacency_list[current_task]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.appendleft(neighbor)

    if len(order) != len(tasks):
        return None

    return order
