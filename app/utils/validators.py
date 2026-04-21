import numpy as np

def validate_features(features):
    if not isinstance(features, list):
        return False

    if len(features) != 4:
        return False

    for f in features:
        if not isinstance(f, (int, float)):
            return False
        if not (-10 <= f <= 10):
            return False

    return True

def sanitize_features(features):
    """
    Defensive preprocessing layer
    - clamps extreme values
    - prevents adversarial spikes
    """

    arr = np.array(features, dtype=float)

    # clamp values to safe ML range
    arr = np.clip(arr, -10, 10)

    return arr.tolist()