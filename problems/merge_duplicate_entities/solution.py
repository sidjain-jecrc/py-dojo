# ============================================================
# Problem: Merge Duplicate Entities
# ============================================================
# An entity resolution system ingests records as plain-text
# strings. Each record describes a named entity with one or
# more identifiers:
#
#   "name=<entity name>|ids=<comma-separated IDs>"
#
# Two entities are considered duplicates if they share at least
# one ID. Duplication is transitive: if entity A shares an ID
# with B, and B shares an ID with C, then A, B, and C are all
# the same logical entity even if A and C share no IDs directly.
#
# Requirements:
#   1. Parse each input string to extract the entity name and
#      its set of IDs.
#   2. Merge all entities that are connected (directly or
#      transitively) through shared IDs.
#   3. For each merged group:
#      - Keep the name of the entity that appeared first
#        (lowest index in the input list).
#      - Combine all IDs into a single sorted list (ascending
#        alphabetical order).
#   4. Return a list of dicts, each with keys "name" (str)
#      and "ids" (list[str]), sorted by "name" alphabetically.
#
# Return type: list[dict]
#
# Example:
#   records = [
#       "name=Airport A|ids=JFK,KJFK",
#       "name=Airport A Duplicate|ids=KJFK,NYC",
#       "name=Airport B|ids=LAX",
#   ]
#
#   Airport A and Airport A Duplicate share ID "KJFK" → merge.
#   Airport B has no overlapping IDs → stays separate.
#
#   Output: [
#       {"name": "Airport A", "ids": ["JFK", "KJFK", "NYC"]},
#       {"name": "Airport B", "ids": ["LAX"]},
#   ]
# ============================================================


def merge_entities(records: list[str]) -> list[dict]:
    raise NotImplementedError
