import requests
import json

hdr = {"X-API-Key": "33a977fc9a604dcca92152e5a4"}
req = requests.get("https://api.checkwx.com/metar/EFHK/decoded", headers=hdr)

print("Response from CheckWX.... \n")

try:
    req.raise_for_status()
    resp = json.loads(req.text)
    print(json.dumps(resp, indent=1))

except requests.exceptions.HTTPError as e:
    print(e)