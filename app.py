from flask import Flask, render_template, redirect, request, url_for, flash
import requests
import json
from pprint import pprint

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/", methods=["POST"])
def search_data():
	city = request.form.get("search")
	checkin = request.form.get("checkin")
	checkout = request.form.get("checkout")
	return redirect(url_for("search_results", city=city, 
											checkin=checkin, 
											checkout=checkout))

@app.route("/search")
def search_results():
	city = request.args.get("city")
	checkin = request.args.get("checkin")
	checkout = request.args.get("checkout")
	xml_request = "<HotelListRequest><destinationstring>"+city+"</destinationstring><arrivalDate>"+checkin+"</arrivalDate><departureDate>"+checkout+"</departureDate></HotelListRequest>"
	payload = {"cid": "55505", "minorRev": "99", 
	 		"apiKey": "pnqbxpnwvest5ap5qrry4pk8", 
	 		"locale": "en_US", "currencyCode": "USD",
	 		"xml": xml_request}
	#headers = {'Content-Type': 'application/json'}
	r = requests.get("http://api.ean.com/ean-services/rs/hotel/v3/list?", params=payload)
	r = json.loads(r.text)
	pprint(r)
	hotel_list = r["HotelListResponse"]["HotelList"]["HotelSummary"]
	return render_template("search.html", city=city, 
										checkin=checkin, 
										checkout=checkout, 
										hotel_list=hotel_list)

if __name__ == "__main__":
	app.run(debug = True)