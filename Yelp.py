#Yelp API

#Business Search  url -- 'https:/api.yelp.com/v3/businesses/search'
#Business Match   url -- 'https:/api.yelp.com/v3/businesses/match'
#Business Phone   url -- 'https:/api.yelp.com/v3/businesses/search/phone/

#Business Details url -- 'https://api.yelp.com/v3/businesses/{id}'
#Business Reviews url -- 'https://api.yelp.com/v3/businesses/{id}/reveiws'

# api to be stolen --  nryKeiIA_hhJyilGu5gem6jFKJHy-UvSLaTTY-aHIpWLwRHJMKEjC9qKUfRND6AHP3J6Bc_M___pIy42YSPApMLl0zv_-ZNIVI64mKvQ33qY3-02wY_56SlZHlL7X3Yx

# Import the modules
import requests
import _json

# Define a business ID
#business_id =

# define the API key, Define the endpoint, and then define the reader
API_Key = 'nryKeiIA_hhJyilGu5gem6jFKJHy-UvSLaTTY-aHIpWLwRHJMKEjC9qKUfRND6AHP3J6Bc_M___pIy42YSPApMLl0zv_-ZNIVI64mKvQ33qY3-02wY_56SlZHlL7X3Yx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_Key}

# define the parameters. key is parameter,
PARAMETERS = {'term':'pizza',
              'limit': 50,
              'radius': 10000,
              'location': 'Philadelphia'}

# make a request to the yelp API_Key
#create a variable to store response
response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

#convert JSON to a dictionary that we can iterate through
business_data = response.json()

for biz in business_data['businesses']:
    print(biz['name'])
    print(biz['url'])
