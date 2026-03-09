import requests
import webbrowser
api="AIzaSyCEm9GOtKIJn0eELBIk1FMZ6bxwFH0Wjlo"
#api=open('apikey').read().strip()
seid=open("seid").read().strip()
inp=input("Enter Search")
search_query=inp
url="https://www.googleapis.com/customsearch/v1"
params={
    'q':search_query,'key':api,'cx':seid}
res=requests.get(url,params=params)
if res.status_code==200:
    result=res.json()
    if 'items' in result and len(result['items'])>0:
        firlink=result['items'][0]['link']
        print("Successful",firlink)
        webbrowser.open(firlink)
    else:
        print("Not Found")
elif res.status_code==400:
    print("Bad Request")
else:
    print("HTTP Error")