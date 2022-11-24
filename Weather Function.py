import requests
import json

hdr = {"X-API-Key": "33a977fc9a604dcca92152e5a4"}

req = requests.get("https://api.checkwx.com/metar/EGLF/decoded", headers=hdr)

print("Response from CheckWX.... \n")

try:
    req.raise_for_status()
    resp = json.loads(req.text)
    #print(json.dumps(resp, indent=1))

    for a in resp['data']:
        print(f'The ICAO code is {resp["data"][0]["icao"]}')
        print(f'Wind is {resp["data"][0]["wind"]["speed_kph"]} kph')
        print(f'The condition: {resp["data"][0]["clouds"][0]["text"]}')
        print(f'Temperature is {resp["data"][0]["temperature"]["celsius"]} degrees Celsius')
except requests.exceptions.HTTPError as e:
    print(e)
