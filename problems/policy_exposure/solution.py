# ============================================================
# Problem: Policy Hierarchy Exposure Calculator
# ============================================================
# Policies are stored as a tree. Each node contributes its
# own base_exposure plus the total exposure of all its
# descendants.
#
# Each node is a dict with:
#   - policy_id      (str)
#   - base_exposure  (int)
#   - children       (list of node dicts — empty list for leaves)
#
# Return a dict mapping every policy_id in the tree to its
# total subtree exposure (base_exposure + sum of all
# descendant subtree exposures).
#
# Example:
#   tree = {
#       "policy_id": "root", "base_exposure": 10,
#       "children": [
#           {"policy_id": "A", "base_exposure": 5,  "children": []},
#           {"policy_id": "B", "base_exposure": 3,
#            "children": [
#                {"policy_id": "C", "base_exposure": 8, "children": []}
#            ]},
#       ]
#   }
#   Output: {"root": 26, "A": 5, "B": 11, "C": 8}
#     root = 10 + 5 + 3 + 8 = 26
#     B    = 3  + 8          = 11
#     A    = 5
#     C    = 8
# ============================================================


def calculate_exposures(root: dict) -> dict[str, int]:
    # Your solution here
    raise NotImplementedError
