# ============================================================
# Problem: Config Inheritance Resolver
# ============================================================
# Configuration values come from three levels, each able to
# override the level below it:
#
#   global_defaults  (lowest priority)
#       ↑ overridden by
#   tenant_overrides
#       ↑ overridden by
#   user_overrides   (highest priority)
#
# Important: a key explicitly set to None IS a valid override.
# It means "this level intentionally clears/nulls this key",
# and must not be skipped during merging.
#
# Input:
#   - global_defaults  (dict)
#   - tenant_overrides (dict)
#   - user_overrides   (dict)
#
# Return a single dict representing the effective config.
# Keys may appear in any combination of the three dicts.
#
# Example:
#   global_defaults  = {"timeout": 30, "retries": 3, "debug": False}
#   tenant_overrides = {"timeout": 60, "debug": None}
#   user_overrides   = {"retries": 5}
#
#   Output: {"timeout": 60, "retries": 5, "debug": None}
#     timeout → tenant wins over global  (60)
#     retries → user wins over global    (5)
#     debug   → tenant explicitly None — that None is the value
# ============================================================


def resolve_config(
    global_defaults: dict,
    tenant_overrides: dict,
    user_overrides: dict,
) -> dict:
    effective_config = {}

    for key, value in global_defaults.items():
        effective_config[key] = value

    for key, value in tenant_overrides.items():
        effective_config[key] = value

    for key, value in user_overrides.items():
        effective_config[key] = value

    return effective_config
 