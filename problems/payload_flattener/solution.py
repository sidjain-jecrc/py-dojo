# ============================================================
# Problem: Nested Claim Payload Flattener
# ============================================================
# Claims arrive as nested dicts that may contain nested dicts,
# lists, or scalar values at any depth. Flatten them into a
# single-level dict using dot-separated keys.
#
# Rules:
#   - Nested dict  → join parent key and child key with "."
#   - List         → use the integer index as the next key component
#   - Scalar value → emit as-is (str, int, bool, None, etc.)
#   - The top-level object is always a dict.
#
# Example:
#   payload = {
#       "claim_id": "C1",
#       "customer": {
#           "name": "Alice",
#           "address": {"city": "Denver", "zip": "80014"}
#       },
#       "documents": [
#           {"type": "form",  "status": "uploaded"},
#           {"type": "photo", "status": "missing"},
#       ],
#   }
#
#   Output: {
#       "claim_id":                "C1",
#       "customer.name":           "Alice",
#       "customer.address.city":   "Denver",
#       "customer.address.zip":    "80014",
#       "documents.0.type":        "form",
#       "documents.0.status":      "uploaded",
#       "documents.1.type":        "photo",
#       "documents.1.status":      "missing",
#   }
# ============================================================

def flatten_payload(payload: dict, separator: str = ".") -> dict:
    # Your solution here
    result = {}

    def flatten(x, parent=''):
        # If the current element is a dictionary, recurse
        if type(x) is dict:
            for a in x:
                flatten(x[a], parent + a + separator)
        # If it's a list, handle by index (optional)
        elif type(x) is list:
            for i, a in enumerate(x):
                flatten(a, parent + str(i) + separator)
        # If it's a value, add to the output dictionary
        else:
            result[parent[:-len(separator)]] = x

    flatten(payload)
    return result
