#weather

import requests
import json

api_key = '695b86f565c2d9468123e937ad407980'
city = 'Philadelphia'
state = 'Pennsylvania'
payload = 'main.temp'

#url
url_id = "http://api.openweathermap.org/data/2.5/weather?q={},{},{}&appid={}".format(city,state,payload,api_key)


response = requests.get('{}'.format(url_id))


if response:
    print("Success!")
else:
    print("Not found")

print(response.text)
