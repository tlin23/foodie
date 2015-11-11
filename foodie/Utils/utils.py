from pykml import parser
import urllib2, re

def parseKML():
	kml_url = 'https://raw.githubusercontent.com/tlin23/foodie/master/foodie/static/files/street_food_vendors.kml'
	fileobject = urllib2.urlopen(kml_url)
	root = parser.parse(fileobject).getroot()

	pmCounter = 1
	lPlacemarks = root.Folder.Placemark
	while pmCounter < len(lPlacemarks):
		sIdRaw = str(lPlacemarks[pmCounter].attrib['id'])
		sNameRaw = str(lPlacemarks[pmCounter].name)
		sDescRaw = str(lPlacemarks[pmCounter].description)
		sCoorRaw = str(lPlacemarks[pmCounter].Point.coordinates)

		nId = int(sIdRaw[4:])
		sName = sNameRaw
		sFoodStyle = parse_food_style(sDescRaw)
		# print sFoodStyle
		sAddress = parse_address(sDescRaw)
		print sAddress
		pmCounter += 1

def parse_food_style(sDescRaw):
	food_style_search_str = 'Food Style: ([a-zA-Z,\s]+?) <br>'
	isFound = re.search(food_style_search_str, sDescRaw)
	if isFound:
		return isFound.groups()[0]

def parse_address(sDescRaw):
	address_search_str = 'Food Style: ([a-zA-Z,\s]+?) <br> ([a-zA-Z0-9\s]+?) <br>'
	isFound = re.search(address_search_str, sDescRaw)
	if isFound:
		return isFound.groups()[1]
	else:
		print sDescRaw
		return