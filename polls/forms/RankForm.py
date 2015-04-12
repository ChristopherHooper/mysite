from django import forms


class RankForm(forms.Form):
    rank = forms.CharField(label='Category Rank', max_length=100)
    searchURI = '/v3/events/10584525601/?token=BKKRDKVUVRC5WG4HAVLT'
	searchCall = protocol +'://'+hostName+searchURI
	for i in range():
		param = rData['categories'][i]["id"]
		rSearch = requests.get(searchCall, params = {'category_id':param})
		print rSearch.json()['organizer']['name']
		
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
					"food":"bacon"
					}				
				}
				)