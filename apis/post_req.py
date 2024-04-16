# POST request

import requests
import json

json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]})
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)
print(post_multi_req.json())
print(type(json_body))
print(json_body)

# data= --> accepts a string (so we had to use json.dumps first)
# json= --> accepts a python dict
