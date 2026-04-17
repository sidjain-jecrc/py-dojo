HINT = {
    "approach": "BFS from the start cell, stop at the first incident reached",
    "time_complexity": "O(R * C)  — each cell visited at most once",
    "space_complexity": "O(R * C)  — visited set + BFS queue",
    "reasoning": """
Standard breadth-first search on a grid.

1. Initialise a queue with the start position and distance 0.
2. Mark the start as visited.
3. While the queue is not empty:
   a. Dequeue (row, col, dist).
   b. If grid[row][col] == "I", return dist.
   c. For each of the four neighbours (up/down/left/right):
      - Skip if out of bounds, blocked ("B"), or already visited.
      - Mark as visited and enqueue with dist + 1.
4. If the queue empties without finding "I", return -1.

BFS guarantees the first incident found is the nearest one
(all edges have weight 1).

Common mistakes:
  - Using DFS instead of BFS — DFS does not guarantee the
    shortest path in an unweighted grid.
  - Forgetting to check whether the start cell itself is "I"
    (should return 0 immediately).
  - Marking cells as visited when dequeued instead of when
    enqueued — causes duplicate entries and wasted work.
""",
}
