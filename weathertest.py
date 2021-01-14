#weather

import requests
import json

api_key = '695b86f565c2d9468123e937ad407980'
city = input(print("What City? >>"))
state = input(print("What State? >>"))

#url
url_id = "http://api.openweathermap.org/data/2.5/weather?q={},{}&units=imperial&appid={}".format(city,state,api_key)

response = requests.get(url_id)
weather_data = json.loads(response.text)

if response:
    pass
else:
    print('Re-enter your location')
    exit()

air_temp = weather_data['main']['temp']
real_feel = weather_data['main']['feels_like']
delta = air_temp - real_feel


print('The air temp is  {0}'.format(air_temp))
print('The real feel is {0}'.format(real_feel))

if air_temp > real_feel:
    print("It's colder than it feels")
else:
    print ("It's warmer than you think")
