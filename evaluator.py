from flask import Flask, render_template, redirect, request, url_for, flash
import MySQLdb
import requests
import json
from pprint import pprint
import time


DB = None
CONN = None

def connect_to_db():
	global DB
	global CONN
	CONN = MySQLdb.connect(host="localhost", user="root", passwd="", db="hotelchains")
	DB = CONN.cursor()


def make_xml_request(destination, checkin, checkout):
	xml_request = "<HotelListRequest><destinationstring>"+destination+"</destinationstring><arrivalDate>"+checkin+"</arrivalDate><departureDate>"+checkout+"</departureDate></HotelListRequest>"
	payload = {"cid": "55505", "minorRev": "99", 
	 		"apiKey": "rddk3k82jjqbk4wgfbkb6qg8",
	 		"locale": "en_US", "currencyCode": "USD",
	 		"xml": xml_request}
 
	 		# "cid": "55505", "minorRev": "99", 
	 		# "apiKey": "pnqbxpnwvest5ap5qrry4pk8", 
	r = requests.get("http://api.ean.com/ean-services/rs/hotel/v3/list?", params=payload)
	r = json.loads(r.text)
	pprint(r)
	return r

#May want to look up some safety stuff since mySQL isn't accepting ? instead of %s
def find_region_code(destination, checkin, checkout):
	connect_to_db()
	query = """SELECT RegionCode FROM RegionCodes WHERE DestinationString = %s"""
	DB.execute(query, (destination,))
	row = DB.fetchone()
	if row:
		code = row[0]
		print "We've already got "+str(code)+" for "+destination
		return code
	else:
		r = make_xml_request(destination,checkin,checkout)
		hotelid = r["HotelListResponse"]["HotelList"]["HotelSummary"][0]["hotelId"]
		query = """SELECT RegionID FROM eanhotellist WHERE eanhotelid = %s"""
		DB.execute(query, (hotelid,))
		row = DB.fetchone()
		code = row[0]
		query = """INSERT INTO RegionCodes (DestinationString, RegionCode) VALUES (%s, %s);"""
		DB.execute(query, (destination,code))
		CONN.commit()
		print "Just added "+str(code)+" for "+destination
		return code
	#connect to DB
	#search for existing string-code match
	#if none, send destination string to expedia api for a hotel id
	#use hotel ID to look up region code
	#write destinationstring and regioncode to DB for future reference


# find_region_code("NYC", "4/7/2014", "4/9/2014")
find_region_code("Austin, TX", "4/7/2014", "4/9/2014")
