import requests
import json
import ssl
import smtplib
import datetime
import csv
from decouple import config

api_key = config('weather_api')
#password = config('mailer_pass')

#global url inherited by each object
#note - to add functionality for more parameters. currently only city, state, apikey & defaulted fahrenheit
url_id = "http://api.openweathermap.org/data/2.5/weather?q={},{}&units=imperial&appid={}"


#define our object
class ListRecipient:
    def __init__(self,email,city,state):
        self.email = email
        self.city = city
        self.state = state
        self.api_url = url_id.format(self.city,self.state,api_key)

    def get_weather_data(self):
        response = requests.get(self.api_url)
        weather_data = json.loads(response.text)
        print(weather_data)  #this prints all JSON data


#these methods don't work - weather_data var isn;t pulled in, so API params
# arent passed through api. will nest or restructure get_weather_data
    #def get_current_temp(self):
    #    current_temp = weather_data['main']['temp']
    #def get_real_feel(self):
    #    real_feel = weather_data['main']['temp']

#create our list of ListRecipients
mailing_list = []

#to convert CSV data into ListReceipient objects, then added to MailingList
with open('mailinglist.csv','r') as read_csv:
    reader = csv.reader(read_csv,delimiter=',')
    for row in reader:
        mailing_list.append(ListRecipient(*row))

for Recipient in mailing_list:
    print(Recipient.get_current_temp)
    print(Recipient.get_current_temp())
