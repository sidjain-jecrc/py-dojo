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

    missing_docs = []
    claim_type = claim["claim_type"]

    # all claims need claim form, check first that
    if "claim_form" not in uploaded_docs:
        missing_docs.append("claim_form")

    if bool(claim["injury"]) and "medical_report" not in uploaded_docs:
        missing_docs.append("medical_report")

    if bool(claim["police_involved"]) and "police_report" not in uploaded_docs:
        missing_docs.append("police_report")

    if claim_type == "auto" and "vehicle_photos" not in uploaded_docs:
        missing_docs.append("vehicle_photos")

    if claim_type == "property" and "property_assessment" not in uploaded_docs:
        missing_docs.append("property_assessment")

    if claim_type == "liability" and "incident_report" not in uploaded_docs:
        missing_docs.append("incident_report")

    missing_docs.sort()
    
    if len(missing_docs) > 0:
        return False, missing_docs
    else:
        return True, missing_docs



