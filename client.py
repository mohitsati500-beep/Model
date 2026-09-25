import requests

data = {
    "iq": 120,
    "cgpa": 8.2
}

response = requests.post(
    "http://127.0.0.1:8000/predict",
    json=data
)

print(response.json())
