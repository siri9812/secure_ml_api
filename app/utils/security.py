import numpy as np

# ----------------------------
# 1. INPUT VALIDATION
# ----------------------------
def validate_features(features):
    if not isinstance(features, list):
        return False

    if len(features) != 4:
        return False

    for x in features:
        if not isinstance(x, (int, float)):
            return False

    return True


# ----------------------------
# 2. INPUT SANITIZATION
# ----------------------------
def sanitize_features(features):
    """
    Defense against adversarial inputs:
    - removes extreme values
    - stabilizes model input
    """

    arr = np.array(features, dtype=float)

    # clamp extreme values (adversarial defense)
    arr = np.clip(arr, -10, 10)

    # optional normalization (stabilizes ML model)
    arr = arr / (np.max(np.abs(arr)) + 1e-6)

    return arr.tolist()