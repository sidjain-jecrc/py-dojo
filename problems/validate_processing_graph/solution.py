# ============================================================
# Problem: Validate Processing Graph
# ============================================================
# A data processing pipeline is defined as a directed graph of
# processing nodes. You receive:
#
#   n     — the expected number of distinct nodes
#   edges — a list of strings in the format "X->Y", each
#           representing a connection between node X and node Y
#
# A valid processing tree must satisfy ALL of the following:
#   1. It contains exactly n distinct nodes.
#   2. It has exactly n - 1 edges.
#   3. All nodes are connected (treating edges as undirected).
#   4. There are no cycles (treating edges as undirected).
#
# Note: edges are parsed as undirected connections for the
# purpose of tree validation.
#
# Special case: n = 1 with no edges is a valid single-node tree.
#
# Function signature:
#   validate_graph(n: int, edges: list[str]) -> bool
#
# Example:
#   n = 4
#   edges = ["A->B", "B->C", "C->D"]
#
#   Nodes: {A, B, C, D} — 4 nodes ✓
#   Edges: 3 = n - 1      ✓
#   Connected: yes         ✓
#   No cycles: yes         ✓
#   Output: True
# ============================================================


def validate_graph(n: int, edges: list[str]) -> bool:
    raise NotImplementedError
