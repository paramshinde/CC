import requests
api='AIzaSyCEm9GOtKIJn0eELBIk1FMZ6bxwFH0Wjlo'
#api=open('apikey').read()
seid=open('seid').read()
searchquery='cat'
url="https://www.googleapis.com/customsearch/v1"
params={'q':searchquery,'key':api,'cx':seid}
res=requests.get(url,params=params)
result=res.json()['items']
for item in result:
    print(item['link'])