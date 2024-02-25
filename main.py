import requests

api_key = 'RGAPI-ea0d7c62-1a63-45a8-aa75-ecde80e4015e'

api_url = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/ALIBABA%20SALUJA'
api_url_key = api_url + '?api_key=' + api_key

response = requests.get(api_url_key)
print(response)

info = response.json()

print(info)