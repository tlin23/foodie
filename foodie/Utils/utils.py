from pykml import parser
import urllib2

def parseKML():
	kml_url = 'http://data.vancouver.ca/download/kml/street_food_vendors.kmz'
	fileobject = urllib2.urlopen(kml_url)
	root = parser.parse(fileobject).getroot()
	print dir(root)