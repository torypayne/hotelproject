import requests
import json
from pprint import pprint

city = "Paris"
checkin = "4/7/2014"
checkout = "4/9/2014"
xml_request = "<HotelListRequest><destinationstring>"+city+"</destinationstring><arrivalDate>"+checkin+"</arrivalDate><departureDate>"+checkout+"</departureDate></HotelListRequest><numberOfResults>25</numberOfResults>"
payload = {"cid": "55505", "minorRev": "99", 
	 		"apiKey": "pnqbxpnwvest5ap5qrry4pk8", 
	 		"locale": "en_US", "currencyCode": "USD",
	 		"xml": xml_request}
r = requests.get("http://api.ean.com/ean-services/rs/hotel/v3/list?", params=payload)
r = json.loads(r.text)
pprint(r)
print type(r)

for i in r["HotelListResponse"]["HotelList"]["HotelSummary"]:
	print i["name"]