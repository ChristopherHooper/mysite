import os
from django.apps import AppConfig
import json
import requests
class MyAppConfig(AppConfig):
	name = 'polls'
	def ready(self):
		Category = self.get_model('Category')
		protocol = 'https'
		hostName = 'www.eventbriteapi.com'
		baseURI = '/v3/categories/?token=BKKRDKVUVRC5WG4HAVLT'
		baseCall = protocol +'://'+hostName+baseURI
		r = requests.get(baseCall)
		rData = r.json()
		dData =[]
		for i in range(len(rData['categories'])):
			dData.append(
				{
				"model": "polls.Category",
				"pk": i,
				"fields":{
					"short_name": rData['categories'][i]["short_name"],
					"CId": rData['categories'][i]["id"],
					"events":" ",
					}				
				}
				)
		filename = os.getcwd() + "fixtures.json"
		if not os.path.exists(os.path.dirname(filename)):
			os.makedirs(os.path.dirname(filename))
		with open(filename, 'w') as outfile:
			json.dump(dData, outfile)