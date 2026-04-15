TEST_CASES = [
    {
        # Basic example from the problem statement.
        "description": "Basic top-2 — distinct frequencies",
        "fn": "top_entities",
        "args": [
            [
                "Hurricane Milton", "Miami", "FEMA",
                "Hurricane Milton", "Miami", "Hurricane Milton",
            ],
            2,
        ],
        "expected": ["Hurricane Milton", "Miami"],
    },
    {
        # All entities mentioned once — lexicographic order breaks the tie.
        "description": "All tied at frequency 1 — lexicographic order",
        "fn": "top_entities",
        "args": [
            ["Delta Airlines", "CBOE", "Atlanta Airport"],
            3,
        ],
        "expected": ["Atlanta Airport", "CBOE", "Delta Airlines"],
    },
    {
        # k = 1 — return only the single most frequent entity.
        "description": "k=1 — return only the top entity",
        "fn": "top_entities",
        "args": [
            ["NATO", "Ukraine", "NATO", "Ukraine", "NATO"],
            1,
        ],
        "expected": ["NATO"],
    },
    {
        # Two entities tied for 2nd place — lex order decides.
        "description": "Tie for 2nd place — lexicographic tiebreaker",
        "fn": "top_entities",
        "args": [
            [
                "SEC", "NYSE", "SEC", "NASDAQ", "NYSE", "NASDAQ", "SEC",
            ],
            3,
        ],
        # SEC=3, NASDAQ=2, NYSE=2 → NASDAQ < NYSE lexicographically
        "expected": ["SEC", "NASDAQ", "NYSE"],
    },
    {
        # Single mention of a single entity.
        "description": "Single entity, single mention",
        "fn": "top_entities",
        "args": [
            ["Earthquake"],
            1,
        ],
        "expected": ["Earthquake"],
    },
    {
        # k equals number of distinct entities — return all, properly ordered.
        "description": "k equals distinct count — return all entities ordered",
        "fn": "top_entities",
        "args": [
            [
                "SpaceX", "NASA", "SpaceX", "Blue Origin",
                "NASA", "SpaceX", "NASA",
            ],
            3,
        ],
        # NASA=3, SpaceX=3, Blue Origin=1 → NASA < SpaceX lex for tie
        "expected": ["NASA", "SpaceX", "Blue Origin"],
    },
    {
        # Large frequency gap between top entity and the rest.
        "description": "One dominant entity with many mentions",
        "fn": "top_entities",
        "args": [
            [
                "Wildfire", "Wildfire", "Wildfire", "Wildfire", "Wildfire",
                "CalFire", "Evacuation", "CalFire",
            ],
            2,
        ],
        # Wildfire=5, CalFire=2, Evacuation=1
        "expected": ["Wildfire", "CalFire"],
    },
    {
        # All entities have the same frequency — pure lexicographic ordering.
        "description": "All entities same frequency — pure lex order, k < distinct",
        "fn": "top_entities",
        "args": [
            [
                "Zephyr", "Monsoon", "Aurora",
                "Zephyr", "Monsoon", "Aurora",
            ],
            2,
        ],
        # Each has 2 mentions. Lex order: Aurora < Monsoon < Zephyr
        "expected": ["Aurora", "Monsoon"],
    },
    {
        # Case sensitivity — "nyc" and "NYC" are different entities.
        "description": "Case-sensitive — 'NYC' and 'nyc' are distinct entities",
        "fn": "top_entities",
        "args": [
            ["NYC", "nyc", "NYC", "nyc", "NYC"],
            2,
        ],
        # NYC=3, nyc=2
        "expected": ["NYC", "nyc"],
    },
    {
        # Realistic multi-entity breaking event scenario.
        "description": "Realistic breaking news — mixed entities and frequencies",
        "fn": "top_entities",
        "args": [
            [
                "Pentagon", "Kyiv", "NATO", "Kyiv", "Pentagon",
                "Zelenskyy", "Kyiv", "NATO", "Zelenskyy",
                "Pentagon", "Kyiv", "NATO",
            ],
            3,
        ],
        # Kyiv=4, NATO=3, Pentagon=3 → NATO < Pentagon lex for tie
        "expected": ["Kyiv", "NATO", "Pentagon"],
    },
]
