import requests

url = "http://127.0.0.1:5000/users/api/1.0/users"
response = requests.get(url)
print (response.text)