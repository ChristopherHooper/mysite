#API relay
import json
import urllib2
'''
> > 1.
> >
> > Create a Django App that presents a user with a set of categories
> > (found here
> > )
> > and asks for the top 3 categories of events they’re interested in. Once
> > they have selected their choices, use the Eventbrite API to gather
> relevant
> > events and display them on a page. The results page should support
> > pagination.
> >
> >
> > Extra Credit: Unit test coverage.
'''
protocol = 'https'
hostname = 'www.eventbriteapi.com'
BaseURI = '/v3/categories/?token=BKKRDKVUVRC5WG4HAVLT'
BaseCall = protocol +'://'+hostname+BaseURI
data = json.load(urllib2.urlopen(BaseCall))
print data
'''
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: Authorization
Content-Type: text/html; charset=utf-8
Allow: GET, HEAD, OPTIONS
'''

