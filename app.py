from flask import Flask, render_template, redirect, request, url_for, flash
import requests

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/", methods=["POST"])
def search_data():
	city = request.form.get("search")
	checkin = request.form.get("checkin")
	checkout = request.form.get("checkout")
	return redirect(url_for("search_results", city=city))

@app.route("/search/<city>")
def search_results(city):
	# xml_request = "<HotelListRequest><destinationstring>"+city+"</destinationstring><arrivalDate>"+checkin+"</arrivalDate><departureDate>"+checkout+"</departureDate></HotelListRequest>"
	# payload = {"cid": "55505", "minorRev": "99", 
	# 		"apiKey": "pnqbxpnwvest5ap5qrry4pk8", 
	# 		"locale": "en_US", "currencyCode": "USD",
	# 		"xml": xml_request}
	# r = requests.get("http://api.ean.com/ean-services/rs/hotel/v3/list?", params=payload)
	# print r.json
	# hotel_json = r.requests.json
	return render_template("search.html", city=city)

if __name__ == "__main__":
	app.run(debug = True)