import json
import requests
import os

def get_events(category_id):
	param = category_id
	print param
	protocol = 'https'
	hostName = 'www.eventbriteapi.com'
	searchURI = '/v3/events/search/?categories='
	token = "&token=BKKRDKVUVRC5WG4HAVLT"
	searchCall = protocol +'://'+hostName+searchURI+param+token
	# I see where you concat'd the value here.  
	rSearch = requests.get(searchCall)
	rData = rSearch.json() 
	array = []
	i = 1
	for event in rData['events']
		
		#-----------
		# why hard coded 6 in above while? <<<<<<<<<<
		#-------------------
		
		num = i*1000+int(category_id)
		print num
		if (if "name" in event):
			if ("description" in event):
				record =  {
					"model": "polls.Eve", 
					"pk": num,
					"fields": { 
						"category" : category_id,
						"name": event["name"]["text"],
						"description": event["description"]["text"],
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
	
