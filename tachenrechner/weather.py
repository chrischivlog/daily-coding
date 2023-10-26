#weather api https://s3.eu-central-1.amazonaws.com/app-prod-static.warnwetter.de/v16/gemeinde_warnings_v2.json
# wir wollen den wert auslesen welche gefahren es aktuell gibt, gibt es nichts ist alles happy und keiner will was von uns LUL 🙃

import requests 
import json

req = requests.get('https://s3.eu-central-1.amazonaws.com/app-prod-static.warnwetter.de/v16/gemeinde_warnings_v2.json')
data = req.text

json = json.loads(data)

parse = json['time']

print(parse)
