import requests

url = "https://dialetus-service.now.sh/regions"
response = requests.get(url)

print(response.text)