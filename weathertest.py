import requests
import json
import ssl
import smtplib

api_key = ''
city = 'Boothwyn'
state = 'Philadelphia'


url_id = "http://api.openweathermap.org/data/2.5/weather?q={},{}&units=imperial&appid={}".format(city,state,api_key)

response = requests.get(url_id)
weather_data = json.loads(response.text)

air_temp = weather_data['main']['temp']
real_feel = weather_data['main']['feels_like']
delta = air_temp - real_feel

#email variables
sender_email = 'rascherbpythontesting@gmail.com'
receiver_email = 'gabbyt321@gmail.com'

message = """\
Subject: Your weather report for {}, {}

It is currently  {} degrees outside
The real feel is {} degrees

Send via python""".format(city,state,air_temp,real_feel)

#encrpytion
port = 465
password = input("Password >>>")

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port,
                        context=context) as server:
    server.login('rascherbpythontesting@gmail.com',password)
    server.sendmail(sender_email,receiver_email,message)
