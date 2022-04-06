
import requests
import json
import pprint
x=requests.get('https://api.merakilearn.org/courses')
pprint.pprint(x.json())
data=x.json()
with open("meraki.json","w") as f:
    json.dump(data,f,indent=4)
    
