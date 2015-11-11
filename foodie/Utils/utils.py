from pykml import parser
import urllib2

def parseKML():
	kml_url = 'https://raw.githubusercontent.com/tlin23/foodie/master/foodie/static/files/street_food_vendors.kml'
	fileobject = urllib2.urlopen(kml_url)
	root = parser.parse(fileobject).getroot()
	print dir(root)