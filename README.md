# 🔐 Secure ML API

## Overview
Production-ready ML API with security controls.

## Features
- JWT Authentication
- Rate Limiting
- Input Validation
- Secure Inference

## Setup
pip install -r requirements.txt

## Train Model
python scripts/train.py

## Run API
uvicorn app.main:app --reload

## Endpoints
- POST /login
- POST /predict