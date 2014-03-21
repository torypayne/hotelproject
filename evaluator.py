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
	r = requests.get("http://api.eancdn.com/ean-services/rs/hotel/v3/list?", params=payload)
	r = json.loads(r.text)
	# pprint(r)
	return r

def request_specific_hotels(hotel_id_list,checkin, checkout):
	hotel_id_list = ",".join([str(i) for i in hotel_id_list])
	xml_request = "<HotelListRequest><hotelIdList>"+hotel_id_list+"</hotelIdList><arrivalDate>"+checkin+"</arrivalDate><departureDate>"+checkout+"</departureDate></HotelListRequest>"
	payload = {"cid": "55505", "minorRev": "99", 
	 		"apiKey": "rddk3k82jjqbk4wgfbkb6qg8",
	 		"locale": "en_US", "currencyCode": "USD",
	 		"xml": xml_request}
	r = requests.get("http://api.eancdn.com/ean-services/rs/hotel/v3/list?", params=payload)
	r = json.loads(r.text)
	# pprint(r)
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


def curated_hotel_list(region):
	hotel_lookup_list = []
	hotel_lookup_detail = {}
	connect_to_db()
	query = """SELECT * FROM CuratedHotels WHERE RegionID = %s"""
	DB.execute(query, (region,))
	rows = DB.fetchall()
	for row in rows:
		eanhotelid = row[1]
		hotel_lookup_detail[eanhotelid] = {}
		hotel_lookup_detail[eanhotelid]["name"] = row[2]
		hotel_lookup_detail[eanhotelid]["website"] = row[13]
		hotel_lookup_detail[eanhotelid]["program"] = row[14]
		hotel_lookup_detail[eanhotelid]["category"] = row[15]
		hotel_lookup_detail[eanhotelid]["points"] = row[16]
		hotel_lookup_detail[eanhotelid]["fifthfree"] = row[17]
		hotel_lookup_detail[eanhotelid]["candp"] = row[18]
		hotel_lookup_detail[eanhotelid]["cashofcandp"] = row[19]
		hotel_lookup_detail[eanhotelid]["pointsofcandp"] = row[20]
		hotel_lookup_detail[eanhotelid]["highseason"] = row[21]
		hotel_lookup_detail[eanhotelid]["highseasondates"] = row[22]
		hotel_lookup_detail[eanhotelid]["highseasonpoints"] = row[23]
		hotel_lookup_detail[eanhotelid]["pointsaverpossible"] = row[24]
		hotel_lookup_detail[eanhotelid]["pointsaverdates"] = row[25]
		hotel_lookup_detail[eanhotelid]["pointsaverpoints"] = row[26]
		hotel_lookup_list.append(eanhotelid)
	return (hotel_lookup_list, hotel_lookup_detail)