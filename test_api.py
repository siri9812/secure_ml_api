import requests

BASE_URL = "http://127.0.0.1:8000"

# login
token = requests.post(f"{BASE_URL}/login").json()["token"]

headers = {
    "Authorization": f"Bearer {token}"
}

# valid input
data = {
    "features":  [9999, -9999, 5000, -3000]
}

response = requests.post(
    f"{BASE_URL}/predict",
    json=data,
    headers=headers
)

print(response.status_code)
print(response.text)



