#API relay
import json
import requests

protocol = 'https'
hostName = 'www.eventbriteapi.com'
baseURI = '/v3/categories/?token=BKKRDKVUVRC5WG4HAVLT'
baseCall = protocol +'://'+hostName+baseURI

r = requests.get(baseCall)
rData = r.json()
for i in range(len(rData['categories'])):
	print rData['categories'][i]["short_name"]

searchURI = '/v3/events/10584525601/?token=BKKRDKVUVRC5WG4HAVLT'
searchCall = protocol +'://'+hostName+searchURI
for i in range(3):
	param = rData['categories'][i]["id"]
	rSearch = requests.get(searchCall, params = {'catagory_id':param})
	print rSearch.json()['organizer']['name']
'''
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: Authorization
Content-Type: text/html; charset=utf-8
Allow: GET, HEAD, OPTIONS
'''

