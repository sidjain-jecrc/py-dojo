# ============================================================
# Problem: Nearest Incident in Grid
# ============================================================
# You are given a 2-D grid representing a facility map. Each
# cell contains one of:
#
#   "E" — empty (passable)
#   "I" — incident location (passable, this is a target)
#   "B" — blocked (impassable)
#
# Given a starting position [row, col], find the minimum number
# of steps to reach the nearest incident ("I") cell. You may
# move one step at a time in four directions: up, down, left,
# right. You cannot move through "B" cells or outside the grid.
#
# Rules:
#   - If the start cell itself is "I", return 0.
#   - If no incident is reachable, return -1.
#   - The start cell is always "E" or "I" (never "B").
#
# Function signature:
#   nearest_incident(grid: list[list[str]], start: list[int]) -> int
#
# Example:
#   grid = [
#       ["E", "E", "B", "I"],
#       ["B", "E", "B", "E"],
#       ["E", "E", "E", "E"],
#       ["I", "B", "E", "E"],
#   ]
#   start = [2, 1]
#
#   Shortest path: (2,1) → (2,0) → (3,0)  [incident]
#   Output: 2
# ============================================================


def nearest_incident(grid: list[list[str]], start: list[int]) -> int:
    raise NotImplementedError
