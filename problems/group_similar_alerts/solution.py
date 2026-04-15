# ============================================================
# Problem: Group Similar Alert Keywords
# ============================================================
# Dataminr's ingestion systems receive noisy user-generated
# text where similar alert keywords may appear in different
# letter arrangements due to OCR issues, scrambled feeds, or
# poor parsing.
#
# You are given a list of short lowercase tokens extracted from
# noisy alerts. Group together all tokens that are anagrams of
# each other, because they likely came from the same corrupted
# source term.
#
# Two strings are anagrams if they contain exactly the same
# characters with the same frequencies, just in a different
# order. For example, "alert" and "later" are anagrams.
#
# Input:
#   - tokens (list[str]): list of lowercase alphabetic strings
#
# Output:
#   - list[list[str]]: a list of groups, where each group is a
#     sorted list of anagram tokens. The groups themselves must
#     be sorted by their first element.
#
# Example:
#   tokens = ["alert", "later", "fire", "rife", "alter"]
#   Output: [["alert", "alter", "later"], ["fire", "rife"]]
#
#   Explanation:
#     "alert", "later", "alter" are all anagrams (sorted letters: "aelrt")
#     "fire", "rife" are anagrams (sorted letters: "efir")
#     Groups sorted by first element: "alert" < "fire"
# ============================================================
from collections import defaultdict


def group_anagrams(tokens: list[str]) -> list[list[str]]:

    anagram_dict = defaultdict(list)
    for token in tokens:
        sorted_token = str(sorted(token))
        # if the sorted token exist, add to the anagram group
        if sorted_token in anagram_dict:
            anagram_dict[sorted_token].append(token)
            continue
        anagram_dict[sorted_token].append(token)

    # record all anagram groups into a single list of list
    result = []
    for _, value in anagram_dict.items():
        result.append(sorted(value))

    # sort the list(list(string)) as well before returning
    return sorted(result)
