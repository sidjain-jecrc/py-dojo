# ============================================================
# Problem: Document Package Completeness Checker
# ============================================================
# Each claim type requires a set of mandatory documents.
# Additional documents may be required based on claim metadata.
#
# Input:
#   - claim: dict with at least:
#       - "claim_type"      (str)  — "auto" | "property" | "liability"
#       - "injury"          (bool) — whether personal injury is involved
#       - "police_involved" (bool) — whether police attended the incident
#   - uploaded_docs: list of document name strings already submitted
#
# Document rules:
#   Base (all claim types):
#       claim_form
#   Auto claims additionally require:
#       vehicle_photos
#   Property claims additionally require:
#       property_assessment
#   Liability claims additionally require:
#       incident_report
#   Conditional (any claim type):
#       injury=True          → medical_report
#       police_involved=True → police_report
#
# Return a tuple (complete, missing) where:
#   - complete (bool):      True if no required documents are missing
#   - missing (list[str]):  sorted list of missing document names
#                           (empty list if complete)
#
# Example:
#   claim = {"claim_type": "auto", "injury": True, "police_involved": False}
#   uploaded_docs = ["claim_form", "vehicle_photos"]
#   # medical_report required because injury=True but not uploaded
#   Output: (False, ["medical_report"])
# ============================================================


def check_completeness(
    claim: dict,
    uploaded_docs: list[str],
) -> tuple[bool, list[str]]:
    # Your solution here
    raise NotImplementedError
