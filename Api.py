import requests
from requests_oauthlib import OAuth1
import json  # Para formato JSON

# GET METHOD 1
print("GET METHOD 1\n")

url = "https://ssd-api.jpl.nasa.gov/fireball.api?limit=20"

payload = {}
headers = {
    'Cookie': 'AWSALBAPP-0=_remove_; AWSALBAPP-1=_remove_; AWSALBAPP-2=_remove_; AWSALBAPP-3=_remove_'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Respuesta JSON con indentación
formatted_response = json.dumps(response.json(), indent=4)
print(formatted_response)

# GET METHOD 2
print("\nGET METHOD 2\n")

url = "https://pokeapi.co/api/v2/pokemon-species/aegislash"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# Formateamos la respuesta JSON con indentación
formatted_response = json.dumps(response.json(), indent=4)
print(formatted_response)

# POST METHOD
print("\nPOST METHOD\n")

# Twitter API v2 endpoint for posting a tweet
url = "https://api.twitter.com/2/tweets"

# Your Twitter API credentials
API_KEY = '2dJnT7jYYrWhW15XmDQ4GJ75P'
API_SECRET_KEY = 'AwFKzJMwuOvcVkFoWaF808rpodVVoOe1Yd55BgRKafp7S8J7dS'
ACCESS_TOKEN = '1894920484547870721-kluOh61kf4TsPiKRHI1EB2x8VGe8WR'
ACCESS_TOKEN_SECRET = 'IteR1vZiLKuMI5LUtkAyVdtdZNlt46wgA34rQeMMg0de4'

# OAuth1 authentication
auth = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# The tweet content
tweet_data = {
    "text": "Este post se hizo con una API :)."
}

# Send the POST request to tweet
response = requests.post(url, json=tweet_data, auth=auth)

# Check the response
if response.status_code == 201:
    print("Post hecho con éxito!")
    # Formateamos la respuesta JSON con indentación
    formatted_response = json.dumps(response.json(), indent=4)
    print(formatted_response)
else:
    print("Intento fallido")
    print(f"Código de estado: {response.status_code}")
    print(f"Respuesta: {response.text}")