from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.core.security import create_token, verify_token
from app.core.rate_limit import is_allowed
from app.services.inference import predict_with_confidence
from app.utils.security import validate_features, sanitize_features
from app.security.anomaly import is_anomalous


app = FastAPI(title="Secure ML API")

security = HTTPBearer()   


@app.get("/")
def home():
    return {"message": "Secure ML API is running"}


@app.post("/login")
def login():
    token = create_token("user")
    return {"token": token}


@app.post("/predict")
def get_prediction(
    data: dict,
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    client_ip = request.client.host

    # 1. Rate limiting
    if not is_allowed(client_ip):
        raise HTTPException(status_code=429, detail="Too many requests")
    
    # 2. Auth check (FIXED)
    token = credentials.credentials

    if not verify_token(token):
        raise HTTPException(status_code=403, detail="Invalid or expired token")

    # 3. Input
    features = data.get("features")

    # 4. Validation
    if not validate_features(features):
        raise HTTPException(status_code=400, detail="Invalid input format")

    # 5. Sanitization (UPGRADE 4) 2. Auth check (FIXED)
    token = credentials.credentials

    if not verify_token(token):
        raise HTTPException(status_code=403, detail="Invalid or expired token")
    features = sanitize_features(features)

    # 6. Adversarial detection
    if is_anomalous(features):
        return {
            "status": "blocked",
            "reason": "Suspicious input detected 🚨"
        }

    # 7. Prediction
    prediction, confidence = predict_with_confidence(features)

    # 8. Confidence check
    if confidence < 0.6:
        return {
            "warning": "Low confidence prediction ⚠️",
            "prediction": prediction,
            "confidence": confidence
        }

    return {
        "prediction": prediction,
        "confidence": confidence
    }

#just in case required local
#if __name__ == "__main__":
 #   import uvicorn
  #  uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

    

