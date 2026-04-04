HINT = {
    "approach": "Three-way dict merge — spread operator or explicit update chain",
    "time_complexity": "O(g + t + u)  — sizes of the three dicts",
    "space_complexity": "O(g + t + u)",
    "reasoning": """
The merge is a straightforward three-way union where later
levels win unconditionally:

    result = {**global_defaults, **tenant_overrides, **user_overrides}

Python's spread operator unpacks dicts left-to-right; a later
key silently overwrites an earlier one, including when the
later value is None. This is exactly the behaviour required.

The common mistake is filtering out None values before merging
(e.g. {k: v for k, v in overrides.items() if v is not None}).
That would break the explicit-None-as-override requirement.
""",
}
