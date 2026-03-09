import requests
def get_loc(api,search):
    base=base="https://us1"
    params={
        'key':api,'q':search,'format':'json'
    }
    res=requests.get(base,params=params)
    data=res.json()
    if res.status_code==200 and data:
        res={'place_id':data[0].get('place_id','),')}


api='pk.d1ad9ee47f879ad713c1e074901bbe41'