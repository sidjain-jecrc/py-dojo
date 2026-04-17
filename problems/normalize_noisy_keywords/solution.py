# ============================================================
# Problem: Normalize Noisy Keywords
# ============================================================
# A data pipeline receives noisy, misspelled keywords that need
# to be normalised to a canonical form. Given a starting keyword
# (possibly misspelled), a target keyword, and a dictionary of
# valid words, find the minimum number of single-character edit
# operations needed to transform `begin` into `end`, where every
# intermediate word after each edit must exist in the dictionary.
#
# Allowed edit operations (one per step):
#   - Substitute one character for another
#   - Insert one character at any position
#   - Delete one character from any position
#
# Rules:
#   - `begin` does NOT need to be in the dictionary.
#   - `end` MUST be in the dictionary.
#   - Each intermediate result after an edit must exist in the
#     dictionary before the next edit can be applied.
#   - Return the minimum number of edit steps, or -1 if no
#     valid transformation sequence exists.
#   - If `begin` == `end`, return 0 (no edits needed).
#
# Function signature:
#   normalize_keyword(begin: str, end: str, dictionary: list[str]) -> int
#
# Example:
#   begin = "flod"
#   end   = "flood"
#   dictionary = ["flood", "floor", "blood", "floods"]
#
#   "flod" → "flood"  (insert 'o' → 1 step)
#   Output: 1
#
# Example 2:
#   begin = "hit"
#   end   = "cog"
#   dictionary = ["hot", "dot", "dog", "lot", "log", "cog"]
#
#   "hit" → "hot" → "dot" → "dog" → "cog"  (4 substitutions)
#   Output: 4
# ============================================================


def normalize_keyword(begin: str, end: str, dictionary: list[str]) -> int:
    raise NotImplementedError
