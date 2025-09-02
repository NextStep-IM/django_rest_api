import requests


endpoint = "http://localhost:8000/api/ping/5"

response = requests.get(endpoint)
print(response.text)
