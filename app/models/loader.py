import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")


def load_model():
    with open("app/models/model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()