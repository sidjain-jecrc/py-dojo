# ============================================================
# Problem: Duplicate Claimant Clustering
# ============================================================
# You are given a list of claimant records. Some records
# represent the same real-world person submitted under
# slightly different details.
#
# Each record is a dict with:
#   - record_id (str)
#   - name      (str)
#   - dob       (str)  — date of birth, e.g. "1990-04-15"
#   - phone     (str)
#   - email     (str)
#
# Two records are considered a match if ANY of the following:
#   1. same phone
#   2. same email
#   3. same normalised name AND same dob
#      (normalise: lowercase and strip leading/trailing whitespace)
#
# Matching is transitive: if A matches B and B matches C,
# then A, B and C all belong to the same cluster — even if
# A and C don't directly share any field.
#
# Return a list of clusters, where each cluster is a sorted
# list of record_ids belonging to the same person.
# The outer list must also be sorted (by each cluster's first
# element) so the result is fully deterministic.
#
# Example:
#   records = [
#       {"record_id": "R1", "name": "Alice",  "dob": "1990-01-01",
#        "phone": "555-0001", "email": "a@x.com"},
#       {"record_id": "R2", "name": "alice ",  "dob": "1990-01-01",
#        "phone": "555-9999", "email": "b@x.com"},   # matches R1 via normalised name + dob
#       {"record_id": "R3", "name": "Bob",    "dob": "1985-06-15",
#        "phone": "555-0002", "email": "bob@x.com"},  # no match with anyone
#   ]
#   Output: [["R1", "R2"], ["R3"]]
# ============================================================


def cluster_claimants(records: list[dict]) -> list[list[str]]:
    # Your solution here
    raise NotImplementedError
