HINT = {
    "approach": "Hash each token by its sorted characters, group with a dict",
    "time_complexity": "O(n * m log m)  — n tokens, m max token length",
    "space_complexity": "O(n)  — storing all tokens in the dict",
    "reasoning": """
For each token, sort its characters to produce a canonical key
(e.g., "later" → "aelrt"). All anagrams share the same key.

Use a defaultdict(list) mapping sorted-key → [tokens].

After one pass, the dict values are the anagram groups.

Sort each group, then sort the list of groups by their first
element to produce deterministic output.

Alternative canonical key: use collections.Counter or a
26-length tuple of character frequencies — avoids the
O(m log m) sort per token, giving O(n * m) overall. For short
tokens the sorted-string approach is simpler and equally fast.

Common mistakes:
  - Forgetting to sort within each group before sorting groups.
  - Using the original token as the key instead of the sorted
    form, which misses the anagram relationship.
  - Not handling duplicate tokens (same string appearing twice).
""",
}
