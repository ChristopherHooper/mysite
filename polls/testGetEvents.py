import json
import requests
import pprint

param = "101"
protocol = 'https'
hostName = 'www.eventbriteapi.com'
searchURI = '/v3/events/search/?categories='
token = "&token=BKKRDKVUVRC5WG4HAVLT"
searchCall = protocol +'://'+hostName+searchURI+param+token
rSearch = requests.get(searchCall)
rData = rSearch.json()
string = rData['events'][0]["organizer"]["logo"]['aspect_ratio']
print string