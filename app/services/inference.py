from app.models.loader import model


def predict(features):
    return int(model.predict([features])[0])


def predict_with_confidence(features):
    """
    Returns prediction + confidence score
    """

    prediction = int(model.predict([features])[0])

    # safe confidence calculation
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba([features])[0]
        confidence = float(max(proba))
    else:
        confidence = 1.0  # fallback

    return prediction, confidence