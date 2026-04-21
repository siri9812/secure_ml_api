# # 🔐 Secure ML API

A production-ready **Machine Learning Inference API** built with FastAPI, designed with multiple layers of security to protect models from abuse, adversarial inputs, and unauthorized access.

---

## 🚀 Overview

This project demonstrates how to deploy a **secure ML model API** with authentication, validation, and attack detection mechanisms. It is designed as a real-world ready backend service for ML inference.

---

## ⚙️ Features

* 🔑 JWT-based Authentication
* 🚦 Rate Limiting (prevents abuse)
* 🧼 Input Validation & Sanitization
* 🚨 Adversarial Input Detection
* ⚠️ Confidence-based Prediction Handling
* 📡 REST API using FastAPI

---

## 🧱 Architecture

Client → Authentication → Rate Limiting → Validation → Sanitization →
Anomaly Detection → ML Model → Response

---

## 📡 API Endpoints

### 🔹 `GET /`

Health check endpoint

### 🔹 `POST /login`

Generates authentication token

### 🔹 `POST /predict`

Secure prediction endpoint

**Headers:**

```
Authorization: Bearer <token>
```

**Request Body:**

```json
{
  "features": [0.5, 1.2, -0.3, 0.8]
}
```

---

## 🧪 Example Usage

```bash
curl -X POST http://127.0.0.1:8000/predict \
-H "Authorization: Bearer <token>" \
-H "Content-Type: application/json" \
-d '{"features": [0.5, 1.2, -0.3, 0.8]}'
```

---

## 🛡️ Security Design

This API implements multiple layers of security:

* Token-based authentication
* Rate limiting
* Input validation
* Feature sanitization
* Adversarial input detection
* Confidence threshold checks

> ⚠️ Sensitive configurations such as secret keys are managed using environment variables and are not stored in the repository.

---

## 🧰 Tech Stack

* Python
* FastAPI
* Uvicorn

---

## 📁 Project Structure

```
secure_ml_api/
├── app/               # Core API logic
├── scripts/           # Training / utility scripts
├── test_api.py        # API testing script
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone repository

```
git clone https://github.com/your-username/secure_ml_api.git
cd secure_ml_api
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```
SECRET_KEY=your_secret_key
```

> ⚠️ Do not commit `.env` to version control

---

### 5. Run the API

```
uvicorn app.main:app --reload
```

---

## ☁️ Deployment

This project can be deployed on cloud platforms like Render using:

* **Build Command:**
  `pip install -r requirements.txt`

* **Start Command:**
  `uvicorn app.main:app --host 0.0.0.0 --port 10000`

---

## 💼 Resume Highlight

Built and deployed a secure ML inference API with authentication, rate limiting, input validation, and adversarial detection using FastAPI.

---

## 📌 Future Improvements

* Distributed rate limiting (Redis)
* Model monitoring and logging
* Docker containerization
* CI/CD integration

---

## 👤 Author

Your Name

Shirisha
