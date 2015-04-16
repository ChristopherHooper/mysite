import json
import requests
import os

def get_events(category_id):
	param = category_id
	print param
	protocol = 'https'
	hostName = 'www.eventbriteapi.com'
	searchURI = '/v3/events/search/?categories=' + category_id
	token = "&token=BKKRDKVUVRC5WG4HAVLT"
	searchCall = protocol +'://'+hostName+searchURI+param+token
	rSearch = requests.get(searchCall)
	rData = rSearch.json() 
	array = []
	i = 1
	while (i<6):
		num = i*1000+int(category_id)
		print num
		if (rData['events'][i]["name"]):
			if (rData['events'][i]["description"]):
				record =  {
					"model": "polls.Eve", 
					"pk": num,
					"fields": { 
						"category" : category_id,
						"name": rData['events'][i]["name"]["text"],
						"description": rData['events'][i]["description"]["text"],
				}}
				array.append(record)
		i += 1
	return array;


protocol = 'https'
hostName = 'www.eventbriteapi.com'
baseURI = '/v3/categories/?token=BKKRDKVUVRC5WG4HAVLT'
baseCall = protocol +'://'+hostName+baseURI
r = requests.get(baseCall)
rData = r.json()
dData =[]
print len(rData['categories'])
for i in range(len(rData['categories'])):
	dData.append(
		{
		"model": "polls.Category",
		"pk": rData['categories'][i]["id"],
		"fields":{
			"short_name": rData['categories'][i]["short_name"],
			"CId": rData['categories'][i]["id"],
			}				
		}
		)
	someV = get_events(rData['categories'][i]["id"])
	dData += someV
filename = "/" + os.getcwd() + "/polls/fixtures/fixtures.json"
#filename = "/Users/Christopher/mysite/polls/fixtures/fixtures.json"
with open(filename, 'w') as outfile:
	json.dump(dData, outfile)
	
