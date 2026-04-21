# 🔐 Secure ML API

A production-ready **Machine Learning Inference API** built with FastAPI, designed with multiple layers of security including authentication, rate limiting, input validation, and adversarial attack detection.

---

## 🚀 Live Demo

🌐 **API Base URL**
https://secure-ml-api.onrender.com

📘 **Interactive Docs (Swagger UI)**
https://secure-ml-api.onrender.com/docs

> ⚠️ Note: This app is hosted on a free tier. The first request may take ~30–50 seconds due to cold start.

---

## ⚙️ Features

* 🔑 JWT Authentication (Token-based access)
* 🚦 Rate Limiting (prevents abuse)
* 🧼 Input Validation & Sanitization
* 🚨 Adversarial Input Detection
* ⚠️ Confidence-based Prediction Filtering
* 📡 RESTful API with FastAPI
* ☁️ Cloud Deployment on Render

---

## 🧱 Architecture

Client
→ Authentication (JWT)
→ Rate Limiting
→ Input Validation
→ Sanitization
→ Anomaly Detection
→ ML Model Inference
→ Response

---

## 📡 API Endpoints

### 🔹 `GET /`

Health check endpoint

---

### 🔹 `POST /login`

Generate authentication token

**Response:**

```json
{
  "token": "your_jwt_token"
}
```

---

### 🔹 `POST /predict`

Secure prediction endpoint

**Headers:**

```
Authorization: Bearer <token>
```

**Request Body:**

```json
{
  "features": [1.0, 2.0, 3.0, 4.0]
}
```

---

## 🧪 Example Usage

### 1️⃣ Get Token

```bash
curl -X POST https://secure-ml-api.onrender.com/login
```

---

### 2️⃣ Make Prediction

```bash
curl -X POST https://secure-ml-api.onrender.com/predict \
-H "Authorization: Bearer <token>" \
-H "Content-Type: application/json" \
-d '{"features": [1, 2, 3, 4]}'
```

---

## 🛡️ Security Design

This API is built with a layered security approach:

* JWT-based authentication
* Rate limiting per client IP
* Input validation and sanitization
* Adversarial input detection
* Confidence threshold filtering

> 🔐 Sensitive data such as `SECRET_KEY` is managed via environment variables and is not stored in the repository.

---

## 🧰 Tech Stack

* Python
* FastAPI
* Uvicorn
* Scikit-learn (for ML model)

---

## 📁 Project Structure

```
secure_ml_api/
├── app/
│   ├── core/        # Security, rate limiting
│   ├── services/    # Inference logic
│   ├── security/    # Anomaly detection
│   ├── utils/       # Validation & sanitization
│   └── main.py      # FastAPI entry point
├── scripts/         # Model training
├── test_api.py      # API testing script
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Local Setup

```bash
git clone https://github.com/siri9812/secure_ml_api.git
cd secure_ml_api

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

---

### 🔐 Environment Variables

Create a `.env` file:

```
SECRET_KEY=your_secure_random_key
```

> ⚠️ Do not commit `.env` to GitHub

---

### ▶️ Run Locally

```bash
uvicorn app.main:app --reload
```

---

## ☁️ Deployment (Render)

* **Build Command:**
  `pip install -r requirements.txt`

* **Start Command:**
  `uvicorn app.main:app --host 0.0.0.0 --port 10000`

* **Environment Variables:**
  `SECRET_KEY` configured in Render dashboard

---

## 💼 Resume Highlight

Developed and deployed a secure ML inference API with JWT authentication, rate limiting, input validation, and adversarial detection using FastAPI and Render.

---

## 📌 Future Improvements

* Redis-based distributed rate limiting
* Docker containerization
* CI/CD pipeline integration
* Model monitoring & logging

---

## 👤 Author

Shirisha Cheruku

---

