TEST_CASES = [
    {
        # Auto claim, no injury, no police. Only base + auto docs needed.
        # All uploaded → complete.
        "description": "Auto claim — all docs present, complete",
        "fn": "check_completeness",
        "args": [
            {"claim_type": "auto", "injury": False, "police_involved": False},
            ["claim_form", "vehicle_photos"],
        ],
        "expected": (True, []),
    },
    {
        # Auto claim with injury. medical_report required but missing.
        "description": "Auto claim with injury — medical_report missing",
        "fn": "check_completeness",
        "args": [
            {"claim_type": "auto", "injury": True, "police_involved": False},
            ["claim_form", "vehicle_photos"],
        ],
        "expected": (False, ["medical_report"]),
    },
    {
        # Auto claim with police involved. police_report required but missing.
        "description": "Auto claim with police — police_report missing",
        "fn": "check_completeness",
        "args": [
            {"claim_type": "auto", "injury": False, "police_involved": True},
            ["claim_form", "vehicle_photos"],
        ],
        "expected": (False, ["police_report"]),
    },
    {
        # Auto claim, both conditionals triggered, both conditional docs missing.
        # claim_form also absent — three documents missing in total.
        "description": "Auto claim — multiple docs missing",
        "fn": "check_completeness",
        "args": [
            {"claim_type": "auto", "injury": True, "police_involved": True},
            ["vehicle_photos"],
        ],
        "expected": (False, ["claim_form", "medical_report", "police_report"]),
    },
    {
        # Property claim, no conditionals, all required docs present.
        "description": "Property claim — complete",
        "fn": "check_completeness",
        "args": [
            {"claim_type": "property", "injury": False, "police_involved": False},
            ["claim_form", "property_assessment"],
        ],
        "expected": (True, []),
    },
    {
        # Property claim missing its type-specific document.
        "description": "Property claim — property_assessment missing",
        "fn": "check_completeness",
        "args": [
            {"claim_type": "property", "injury": False, "police_involved": False},
            ["claim_form"],
        ],
        "expected": (False, ["property_assessment"]),
    },
    {
        # Property claim with police involved. police_report missing.
        "description": "Property claim with police — police_report missing",
        "fn": "check_completeness",
        "args": [
            {"claim_type": "property", "injury": False, "police_involved": True},
            ["claim_form", "property_assessment"],
        ],
        "expected": (False, ["police_report"]),
    },
    {
        # Liability claim, all docs present including conditionals.
        "description": "Liability claim with injury and police — complete",
        "fn": "check_completeness",
        "args": [
            {"claim_type": "liability", "injury": True, "police_involved": True},
            ["claim_form", "incident_report", "medical_report", "police_report"],
        ],
        "expected": (True, []),
    },
    {
        # Liability claim, nothing uploaded at all.
        "description": "Liability claim with injury and police — nothing uploaded",
        "fn": "check_completeness",
        "args": [
            {"claim_type": "liability", "injury": True, "police_involved": True},
            [],
        ],
        "expected": (False, ["claim_form", "incident_report", "medical_report", "police_report"]),
    },
    {
        # Extra documents uploaded beyond what is required — should still be complete.
        "description": "Extra documents uploaded — still complete",
        "fn": "check_completeness",
        "args": [
            {"claim_type": "auto", "injury": False, "police_involved": False},
            ["claim_form", "vehicle_photos", "extra_letter", "selfie.jpg"],
        ],
        "expected": (True, []),
    },
    {
        # Liability claim, no conditionals, only base doc uploaded (incident_report missing).
        "description": "Liability claim — incident_report missing",
        "fn": "check_completeness",
        "args": [
            {"claim_type": "liability", "injury": False, "police_involved": False},
            ["claim_form"],
        ],
        "expected": (False, ["incident_report"]),
    },
]
