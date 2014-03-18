# import os
import MySQLdb
import requests
import json
from pprint import pprint
import time

# connect
# dbpw = os.environ.get('SUDOPW')
DB = None
CONN = None

tried_list = []

# execute SQL select statement
# result = cursor.execute("select * from ratetesting")

# print result

# # # commit your changes
# # db.commit()

# # get the number of rows in the resultset
# numrows = int(cursor.rowcount)

# # get and display one row at a time.
# for x in range(0,numrows):
#     row = cursor.fetchone()
#     print row[0], "-->", row[1]
def create_hotel_list():
    print DB
    # limit = str(limit)
    query = """SELECT EANHotelID FROM eanhotellist WHERE TripAdvisorRating IS NULL LIMIT 50"""
    DB.execute(query)
    # row = DB.fetchone()
    # print row
    rows = DB.fetchall()
    grades = {}
    hotels_to_pull = ""
    for i in range(len(rows)):
    	idstring = str(rows[i][0])
    	idstring = idstring.replace("L", "")
    	if idstring in tried_list:
    		set_ta_to_one(idstring)
    	else:
    		# print idstring
    		hotels_to_pull = hotels_to_pull+","+idstring
    		tried_list.append(idstring)
    		# hotels_to_pull = hotels_to_pull + "," + idstring
    hotels_to_pull = hotels_to_pull[1:]
    # print hotels_to_pull
    return hotels_to_pull
    # pass
	#join

def set_ta_to_one(ean_hotel_id):
	query = """UPDATE eanhotellist SET tripAdvisorRating = 1 WHERE eanhotelid = %s"""
	DB.execute(query, (ean_hotel_id,))
	print "Just set TA rating to one for "+str(ean_hotel_id)


def make_xml_request(hotel_id_list):
	checkin = "5/7/2014"
	checkout = "5/11/2014"
	print hotel_id_list
	xml_request = "<HotelListRequest><hotelIdList>"+hotel_id_list+"</hotelIdList><arrivalDate>"+checkin+"</arrivalDate><departureDate>"+checkout+"</departureDate></HotelListRequest>"
	payload = {"cid": "55505", "minorRev": "99", 
	 		"apiKey": "pnqbxpnwvest5ap5qrry4pk8", 
	 		"locale": "en_US", "currencyCode": "USD",
	 		"xml": xml_request}
	print xml_request
	r = requests.get("http://api.ean.com/ean-services/rs/hotel/v3/list?", params=payload)
	r = json.loads(r.text)
	# pprint(r)
	try:
		hotel_list = r["HotelListResponse"]["HotelList"]["HotelSummary"]
		# pprint(hotel_list)
		if isinstance(hotel_list,list): 
			return hotel_list
		else:
			hotel_list = [hotel_list]
			return hotel_list
	except:
		hotel_id_list = hotel_id_list.split(",")
		for i in range(len(hotel_id_list)):
			set_ta_to_one(hotel_id_list[i])
	

def update_db_TA_price(hotel_list):
	# print type(hotel_list)
	for i in range(len(hotel_list)):
		try:
			ean_id = hotel_list[i]["hotelId"]
			ta_rating = hotel_list[i]["tripAdvisorRating"]
			avg_price = hotel_list[i]["RoomRateDetailsList"]["RoomRateDetails"]["RateInfos"]["RateInfo"]["ChargeableRateInfo"]["@averageRate"]
			print ean_id
			print ta_rating
			print avg_price
			query = """UPDATE eanhotellist SET tripAdvisorRating = %s WHERE eanhotelid = %s"""
			DB.execute(query, (ta_rating,ean_id))
			query = """UPDATE eanhotellist SET PulledAvgPrice = %s WHERE eanhotelid = %s"""
			DB.execute(query, (ta_rating,avg_price))
		except:
			print "Something didn't work"
			try:
				print ean_id
				# query = """UPDATE eanhotellist SET tripAdvisorRating = 1 WHERE eanhotelid = %s"""
				# DB.execute(query, (ean_id))
			except:
				print "I couldn't even print the ean_id"


def connect_to_db():
	global DB
	global CONN
	CONN = MySQLdb.connect(host="localhost", user="root", passwd="", db="hotelchains")
	DB = CONN.cursor()
	print DB

def main():
	connect_to_db()
	command = None	
	while command != "quit":
		hotel_ids = create_hotel_list()
		# hotel_ids = str(152405)+","+str(174419)
		hotels = make_xml_request(hotel_ids)
		if hotels != None:
			update_db_TA_price(hotels) 	
		CONN.commit()
		print "I just wrote to the database"
		time.sleep(1)
	CONN.close()

if __name__ == "__main__":
    main()