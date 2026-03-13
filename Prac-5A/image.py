#search image
import requests
'''
API_KEY = open("API_KEY").read()
SEARCH_ENGINE_ID = open("SEARCH_ENGINE_ID").read()'''

API_KEY='AIzaSyBORUlQGEbvXY2cf2C2CNsHMltN6OL6Qpc'
SEARCH_ENGINE_ID='834678b62e59a4602'

search_query = "car"

url = "https://www.googleapis.com/customsearch/v1"

params = {
    'q': search_query,
    'key': API_KEY,
    'cx': SEARCH_ENGINE_ID,
    'searchType': 'image'
}

response = requests.get(url, params=params)
results = response.json()['items']

for item in results:
    print(item['link'])

API_KEY='AIzaSyBORUlQGEbvXY2cf2C2CNsHMltN6OL6Qpc'
SEARCH_ENGINE_ID='834678b62e59a4602'