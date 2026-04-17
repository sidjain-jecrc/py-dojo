HINT = {
    "approach": "BFS from begin, neighbours are dict words within edit distance 1",
    "time_complexity": "O(n * m^2)  — n words, m max word length",
    "space_complexity": "O(n * m)  — dictionary set + BFS queue",
    "reasoning": """
Put the dictionary into a set for O(1) lookup.

BFS from `begin`, exploring one level (one edit) at a time.
For each current word, generate ALL possible single-edit
neighbours:
  - Substitutions: for each position, try all 25 other chars.
  - Insertions: for each of (len+1) positions, try all 26 chars.
  - Deletions: for each position, remove the char.

If a generated word is in the dictionary set AND hasn't been
visited, enqueue it. When `end` is dequeued, return the current
BFS depth (number of edit steps).

Generating neighbours is O(m * 26) per word, and checking
membership in the set is O(m). Each word is visited at most
once, so overall work is O(n * m * 26 * m) ≈ O(n * m^2).

Common mistakes:
  - Computing edit distance between all pairs: O(n^2 * m^2),
    much slower than the generation approach.
  - Forgetting to handle words of different lengths (need
    insert/delete, not just substitution).
  - Not marking words as visited when enqueued (causes
    duplicate processing and TLE).
""",
}
