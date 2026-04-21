import numpy as np

def is_anomalous(features):
    """
    Basic anomaly detection using statistical bounds
    """

    arr = np.array(features)

    # Rule 1: too large values = suspicious
    if np.any(arr > 100) or np.any(arr < -100):
        return True

    # Rule 2: extreme variance = suspicious
    if np.std(arr) > 50:
        return True

    return False