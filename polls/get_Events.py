import json
import requests

def get_events(category_id):
	param = category_id
	protocol = 'https'
	hostName = 'www.eventbriteapi.com'
	searchURI = '/v3/events/search/?categories='
	token = "&token=BKKRDKVUVRC5WG4HAVLT"
	searchCall = protocol +'://'+hostName+searchURI+param+token
	rSearch = requests.get(searchCall)
	rData = rSearch.json()
	data = []
	for i in range(5):
		data.append(
				{
					"name": rData['events'][i]["name"]["text"],
					"description": rData['events'][i]["description"]["text"],
				}
				)
	return data