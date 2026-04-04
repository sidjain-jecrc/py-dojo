HINT = {
    "approach": "Recursive DFS (or iterative stack) with a running key prefix",
    "time_complexity": "O(n)  — n total values across all nesting levels",
    "space_complexity": "O(d)  — d is the maximum nesting depth (call stack)",
    "reasoning": """
Define a helper that takes the current value and its accumulated
key prefix. Three cases:

  dict  → recurse for each (k, v) with prefix = parent_prefix + sep + k
  list  → recurse for each (i, v) with prefix = parent_prefix + sep + str(i)
  scalar → emit (prefix, value) into the result dict

Start with an empty prefix for each top-level key so the root
keys have no leading separator.

An iterative version using a stack of (prefix, value) pairs
avoids Python's recursion limit for deeply nested payloads and
is otherwise identical in logic.

The common mistake is using string concatenation inside the loop
without stripping a leading separator from the root keys — keep
the prefix-building conditional on whether prefix is empty.
""",
}
