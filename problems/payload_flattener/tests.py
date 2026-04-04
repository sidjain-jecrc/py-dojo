TEST_CASES = [
    {
        # Already flat — output equals input.
        "description": "Flat dict — no nesting, output unchanged",
        "fn": "flatten_payload",
        "args": [{"claim_id": "C1", "status": "open", "amount": 500}],
        "expected": {"claim_id": "C1", "status": "open", "amount": 500},
    },
    {
        # One level of nesting.
        "description": "One level of nested dict",
        "fn": "flatten_payload",
        "args": [{
            "claim_id": "C1",
            "customer": {"name": "Alice", "age": 30},
        }],
        "expected": {
            "claim_id": "C1",
            "customer.name": "Alice",
            "customer.age": 30,
        },
    },
    {
        # Two levels of nesting.
        "description": "Two levels of nested dicts",
        "fn": "flatten_payload",
        "args": [{
            "customer": {
                "address": {"city": "Denver", "zip": "80014"},
            },
        }],
        "expected": {
            "customer.address.city": "Denver",
            "customer.address.zip": "80014",
        },
    },
    {
        # List of scalars — indices become key components.
        "description": "List of scalar values",
        "fn": "flatten_payload",
        "args": [{"tags": ["fraud", "urgent", "auto"]}],
        "expected": {
            "tags.0": "fraud",
            "tags.1": "urgent",
            "tags.2": "auto",
        },
    },
    {
        # List of dicts — full example from the problem statement.
        "description": "List of dicts — documents example",
        "fn": "flatten_payload",
        "args": [{
            "claim_id": "C1",
            "customer": {
                "name": "Alice",
                "address": {"city": "Denver", "zip": "80014"},
            },
            "documents": [
                {"type": "form",  "status": "uploaded"},
                {"type": "photo", "status": "missing"},
            ],
        }],
        "expected": {
            "claim_id":              "C1",
            "customer.name":         "Alice",
            "customer.address.city": "Denver",
            "customer.address.zip":  "80014",
            "documents.0.type":      "form",
            "documents.0.status":    "uploaded",
            "documents.1.type":      "photo",
            "documents.1.status":    "missing",
        },
    },
    {
        # None value at a leaf — should be preserved, not skipped.
        "description": "None as a leaf value — preserved",
        "fn": "flatten_payload",
        "args": [{"customer": {"middle_name": None}}],
        "expected": {"customer.middle_name": None},
    },
    {
        # Boolean leaf values.
        "description": "Boolean leaf values — preserved",
        "fn": "flatten_payload",
        "args": [{"flags": {"is_fraud": True, "is_duplicate": False}}],
        "expected": {"flags.is_fraud": True, "flags.is_duplicate": False},
    },
    {
        # Empty nested dict — produces no keys for that subtree.
        "description": "Empty nested dict — contributes no keys",
        "fn": "flatten_payload",
        "args": [{"claim_id": "C1", "metadata": {}}],
        "expected": {"claim_id": "C1"},
    },
    {
        # Empty list — produces no keys for that subtree.
        "description": "Empty list — contributes no keys",
        "fn": "flatten_payload",
        "args": [{"claim_id": "C1", "documents": []}],
        "expected": {"claim_id": "C1"},
    },
    {
        # List containing a mix of scalars and dicts.
        "description": "Mixed list — scalars and dicts",
        "fn": "flatten_payload",
        "args": [{"items": ["note", {"key": "value"}, 42]}],
        "expected": {
            "items.0":     "note",
            "items.1.key": "value",
            "items.2":     42,
        },
    },
    {
        # Custom separator.
        "description": "Custom separator — double underscore",
        "fn": "flatten_payload",
        "args": [
            {"a": {"b": {"c": 1}}},
            "__",
        ],
        "expected": {"a__b__c": 1},
    },
]
