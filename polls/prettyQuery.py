from .models import Category, Eve

def prettyQuery(category_Id):
	pretty = ""
	catSet = Category.objects.filter(CId = category_Id)
	for i in catSet:
		pretty += "<h1 style='font-family:verdana'>\nCategory: " + i.short_name +" </h1>"
	pretty +="<ol>"
	querySet = Eve.objects.filter(category = category_Id)
	for i in querySet:
		pretty += "<br><li>\n Event Name: " + i.name + "</li><ul>"
		pretty += "<br><li>\n Event description: " + i.description+ "</li></ul>"
	pretty += "</ol>"
	return pretty
