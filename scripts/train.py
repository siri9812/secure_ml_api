from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

os.makedirs("app/models", exist_ok=True)

data = load_iris()
X, y = data.data, data.target

model = RandomForestClassifier()
model.fit(X, y)

with open("app/models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved!")