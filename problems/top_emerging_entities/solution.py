# ============================================================
# Problem: Top Emerging Entities in Breaking Events
# ============================================================
# Dataminr ingests a stream of real-time events from news
# reports, social posts, emergency feeds, and public data
# sources. Each event may mention one or more named entities
# such as cities, airports, political leaders, companies, or
# weather systems.
#
# You are given a list of entity mentions collected over the
# last 10 minutes. Return the top K most frequently mentioned
# entities.
#
# If two entities have the same frequency, return the one with
# the lexicographically smaller name first.
#
# Input:
#   - mentions (list[str]): list of entity name strings
#     (may contain duplicates)
#   - k (int): number of top entities to return (1 <= k <= number
#     of distinct entities)
#
# Output:
#   - list[str]: the top K entity names, ordered by frequency
#     descending, then lexicographically ascending for ties.
#
# Example:
#   mentions = [
#       "Hurricane Milton", "Miami", "FEMA",
#       "Hurricane Milton", "Miami", "Hurricane Milton",
#   ]
#   k = 2
#   Output: ["Hurricane Milton", "Miami"]
#
#   Explanation:
#     Hurricane Milton → 3 mentions
#     Miami            → 2 mentions
#     FEMA             → 1 mention
#     Top 2 by frequency: ["Hurricane Milton", "Miami"]
# ============================================================
from collections import defaultdict


def top_entities(mentions: list[str], k: int) -> list[str]:

    mention_map = defaultdict(int)
    for mention in mentions:
        if mention in mention_map:
            mention_map[mention] += 1
        else:
            mention_map[mention] = 1

    sorted_map = dict(sorted(mention_map.items(), key=lambda item: (-item[1], item[0])))
    top_k = list(sorted_map.keys())[:k]

    return top_k