from flask import Flask, render_template, redirect, request, url_for, flash
import requests
import json
from pprint import pprint
import evaluator


app = Flask(__name__)
app.secret_key = "tempsecret"

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
	region = evaluator.find_region_code(city, checkin, checkout)
	hotel_tuple = evaluator.curated_hotel_list(region)
	hotel_list = hotel_tuple[0]
	hotel_dict = hotel_tuple[1]
	r = evaluator.request_specific_hotels(hotel_list,checkin,checkout)
	try:
		hotel_list = r["HotelListResponse"]["HotelList"]["HotelSummary"]
		return render_template("search.html", city=city, 
											checkin=checkin, 
											checkout=checkout, 
											hotel_list=hotel_list)
	except:
		flash("Oh no! We couldn't find any hotels that matched your request! Double check your destination spelling and specificity, then try different dates.")
		return redirect(url_for("index"))
	# flash("You made it past to the end of your code!")
	# return redirect(url_for("index"))

if __name__ == "__main__":
	app.run(debug = True)