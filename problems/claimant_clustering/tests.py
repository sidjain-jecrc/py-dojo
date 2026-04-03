TEST_CASES = [
    {
        # Two records share a phone number — one cluster.
        "description": "Same phone — two records merge into one cluster",
        "fn": "cluster_claimants",
        "args": [[
            {"record_id": "R1", "name": "Alice",   "dob": "1990-01-01", "phone": "555-0001", "email": "alice@a.com"},
            {"record_id": "R2", "name": "A. Smith", "dob": "1985-03-10", "phone": "555-0001", "email": "asmith@b.com"},
        ]],
        "expected": [["R1", "R2"]],
    },
    {
        # Two records share an email — one cluster.
        "description": "Same email — two records merge into one cluster",
        "fn": "cluster_claimants",
        "args": [[
            {"record_id": "R1", "name": "Bob",     "dob": "1978-07-04", "phone": "555-1111", "email": "shared@mail.com"},
            {"record_id": "R2", "name": "Robert",  "dob": "1978-07-04", "phone": "555-2222", "email": "shared@mail.com"},
        ]],
        "expected": [["R1", "R2"]],
    },
    {
        # Same normalised name and dob — one cluster.
        # Name differs only in case and trailing whitespace.
        "description": "Same normalised name + dob — two records merge",
        "fn": "cluster_claimants",
        "args": [[
            {"record_id": "R1", "name": "Carol Jones",  "dob": "2000-12-25", "phone": "555-3333", "email": "c1@x.com"},
            {"record_id": "R2", "name": "carol jones ", "dob": "2000-12-25", "phone": "555-4444", "email": "c2@x.com"},
        ]],
        "expected": [["R1", "R2"]],
    },
    {
        # No fields overlap — every record is its own cluster.
        "description": "No matches — each record is its own cluster",
        "fn": "cluster_claimants",
        "args": [[
            {"record_id": "R1", "name": "Alice",   "dob": "1990-01-01", "phone": "555-0001", "email": "alice@a.com"},
            {"record_id": "R2", "name": "Bob",     "dob": "1985-06-15", "phone": "555-0002", "email": "bob@b.com"},
            {"record_id": "R3", "name": "Charlie", "dob": "1972-03-22", "phone": "555-0003", "email": "charlie@c.com"},
        ]],
        "expected": [["R1"], ["R2"], ["R3"]],
    },
    {
        # Transitive match: R1–R2 share phone, R2–R3 share email.
        # R1 and R3 share no field directly but must be in the same cluster.
        "description": "Transitive merge — R1-R2 via phone, R2-R3 via email",
        "fn": "cluster_claimants",
        "args": [[
            {"record_id": "R1", "name": "Dave",  "dob": "1995-08-30", "phone": "555-7777", "email": "dave1@x.com"},
            {"record_id": "R2", "name": "David", "dob": "1990-01-01", "phone": "555-7777", "email": "shared@x.com"},
            {"record_id": "R3", "name": "D.K.",  "dob": "1980-05-05", "phone": "555-8888", "email": "shared@x.com"},
        ]],
        "expected": [["R1", "R2", "R3"]],
    },
    {
        # Two separate clusters, no links between them.
        "description": "Two distinct clusters — no cross-cluster matches",
        "fn": "cluster_claimants",
        "args": [[
            {"record_id": "R1", "name": "Eve",   "dob": "1988-02-14", "phone": "555-1001", "email": "eve@a.com"},
            {"record_id": "R2", "name": "Eve",   "dob": "1988-02-14", "phone": "555-1002", "email": "eve2@a.com"},
            {"record_id": "R3", "name": "Frank", "dob": "1970-11-30", "phone": "555-2001", "email": "frank@b.com"},
            {"record_id": "R4", "name": "Frank", "dob": "1970-11-30", "phone": "555-2002", "email": "frank2@b.com"},
        ]],
        "expected": [["R1", "R2"], ["R3", "R4"]],
    },
    {
        # Long transitive chain: R1→R2 (phone), R2→R3 (email), R3→R4 (name+dob).
        # All four should land in the same cluster.
        "description": "Four-record transitive chain — all one cluster",
        "fn": "cluster_claimants",
        "args": [[
            {"record_id": "R1", "name": "Gina",  "dob": "1993-03-03", "phone": "555-AAAA", "email": "g1@x.com"},
            {"record_id": "R2", "name": "G. Lee", "dob": "1985-07-07", "phone": "555-AAAA", "email": "g2@x.com"},
            {"record_id": "R3", "name": "Harry",  "dob": "1960-01-01", "phone": "555-BBBB", "email": "g2@x.com"},
            {"record_id": "R4", "name": "harry",  "dob": "1960-01-01", "phone": "555-CCCC", "email": "h4@x.com"},
        ]],
        "expected": [["R1", "R2", "R3", "R4"]],
    },
    {
        # Single record — trivial single-element cluster.
        "description": "Single record — one cluster of one",
        "fn": "cluster_claimants",
        "args": [[
            {"record_id": "R1", "name": "Iris", "dob": "2001-09-09", "phone": "555-0000", "email": "iris@i.com"},
        ]],
        "expected": [["R1"]],
    },
    {
        # Name matches only when BOTH normalised name AND dob match.
        # Here name is the same but dob differs — should NOT merge.
        "description": "Same name but different dob — no merge",
        "fn": "cluster_claimants",
        "args": [[
            {"record_id": "R1", "name": "Jane Doe", "dob": "1990-05-01", "phone": "555-1111", "email": "j1@x.com"},
            {"record_id": "R2", "name": "Jane Doe", "dob": "1991-05-01", "phone": "555-2222", "email": "j2@x.com"},
        ]],
        "expected": [["R1"], ["R2"]],
    },
]
