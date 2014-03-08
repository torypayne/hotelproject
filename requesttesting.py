import requests


payload = {"cid": "55505", "minorRev": "99", 
			"apiKey": "pnqbxpnwvest5ap5qrry4pk8", 
			"locale": "en_US", "currencyCode": "USD",
			"xml": "<HotelListRequest><destinationstring>Paris</destinationstring><arrivalDate>4/7/2014</arrivalDate><departureDate>4/9/2014</departureDate></HotelListRequest>"}

r = requests.get("http://api.ean.com/ean-services/rs/hotel/v3/list?", params=payload)
r.json()
print r
