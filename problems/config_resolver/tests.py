TEST_CASES = [
    {
        # Basic three-level override — each key comes from a different level.
        "description": "Basic inheritance — one key per level",
        "fn": "resolve_config",
        "args": [
            {"timeout": 30, "retries": 3, "debug": False},
            {"timeout": 60},
            {"retries": 5},
        ],
        "expected": {"timeout": 60, "retries": 5, "debug": False},
    },
    {
        # User wins over both tenant and global for the same key.
        "description": "User overrides tenant overrides global — same key",
        "fn": "resolve_config",
        "args": [
            {"max_connections": 10},
            {"max_connections": 20},
            {"max_connections": 50},
        ],
        "expected": {"max_connections": 50},
    },
    {
        # Tenant explicitly sets a key to None.
        # User does not mention that key, so None must survive.
        "description": "Tenant sets key to None — None is preserved as value",
        "fn": "resolve_config",
        "args": [
            {"feature_flag": True, "timeout": 30},
            {"feature_flag": None},
            {},
        ],
        "expected": {"feature_flag": None, "timeout": 30},
    },
    {
        # User sets a key to None, overriding a non-None tenant value.
        "description": "User sets key to None — overrides tenant's real value",
        "fn": "resolve_config",
        "args": [
            {"log_level": "INFO"},
            {"log_level": "DEBUG"},
            {"log_level": None},
        ],
        "expected": {"log_level": None},
    },
    {
        # Tenant sets to None, user restores a real value.
        # User's real value wins — None from tenant is overridden.
        "description": "User restores value that tenant nulled",
        "fn": "resolve_config",
        "args": [
            {"rate_limit": 100},
            {"rate_limit": None},
            {"rate_limit": 200},
        ],
        "expected": {"rate_limit": 200},
    },
    {
        # Key only in tenant — not in global or user.
        "description": "Key introduced at tenant level — no global or user entry",
        "fn": "resolve_config",
        "args": [
            {"global_only": "g"},
            {"tenant_only": "t"},
            {},
        ],
        "expected": {"global_only": "g", "tenant_only": "t"},
    },
    {
        # Key only in user — not in global or tenant.
        "description": "Key introduced at user level — no global or tenant entry",
        "fn": "resolve_config",
        "args": [
            {},
            {},
            {"user_only": "u"},
        ],
        "expected": {"user_only": "u"},
    },
    {
        # All three dicts are empty — result is empty.
        "description": "All empty dicts — empty config",
        "fn": "resolve_config",
        "args": [{}, {}, {}],
        "expected": {},
    },
    {
        # Realistic scenario — mixed keys, mixed None overrides.
        "description": "Realistic scenario — mixed keys and None overrides",
        "fn": "resolve_config",
        "args": [
            {"timeout": 30, "retries": 3, "debug": False, "max_size": 1024},
            {"timeout": 60, "debug": None, "region": "us-east-1"},
            {"retries": 1, "region": "eu-west-1"},
        ],
        "expected": {
            "timeout": 60,
            "retries": 1,
            "debug": None,
            "max_size": 1024,
            "region": "eu-west-1",
        },
    },
]
