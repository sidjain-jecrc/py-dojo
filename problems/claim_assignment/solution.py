# ============================================================
# Problem: Claim Assignment Balancing
# ============================================================
# A claims platform receives new claims throughout the day.
#
# Each claim is a dict with:
#   - claim_id       (str)
#   - complexity     (int)  — added to specialist's load on assignment
#   - required_skills (set of str)
#
# Each specialist is a dict with:
#   - specialist_id  (str)
#   - skills         (set of str)
#   - current_load   (int)
#
# Assign each claim to an eligible specialist such that:
#   1. The specialist has ALL required skills for the claim.
#   2. The final assignment keeps workloads as balanced as possible.
#      (Greedy: always assign to the currently least-loaded eligible specialist.)
#   3. Tie-break: if multiple eligible specialists share the lowest load,
#      choose the lexicographically smallest specialist_id.
#
# Claims are processed in the order given. Assigning a claim adds
# its complexity to the chosen specialist's running load.
#
# Return a dict mapping claim_id -> specialist_id.
#
# Example:
#   claims = [
#       {"claim_id": "C1", "complexity": 3, "required_skills": {"python"}},
#       {"claim_id": "C2", "complexity": 2, "required_skills": {"python"}},
#   ]
#   specialists = [
#       {"specialist_id": "alice", "skills": {"python"}, "current_load": 0},
#       {"specialist_id": "bob",   "skills": {"python"}, "current_load": 0},
#   ]
#   # C1: alice and bob both at load 0 → pick "alice" (lex smaller), load becomes 3
#   # C2: alice at 3, bob at 0 → pick "bob", load becomes 2
#   Output: {"C1": "alice", "C2": "bob"}
# ============================================================


def assign_claims(claims: list[dict], specialists: list[dict]) -> dict[str, str]:
    # Your solution here
    raise NotImplementedError
