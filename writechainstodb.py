import json
from pprint import pprint
import MySQLdb

DB = None
CONN = None

def connect_to_db():
	global DB
	global CONN
	CONN = MySQLdb.connect(host="localhost", user="root", passwd="", db="hotelchains")
	DB = CONN.cursor()
	print DB


connect_to_db()

json_data=open('hoteldictionary.json')

data = json.load(json_data)

counter = 0
fails = 0
success = 0

failedmatches = {}


for i in data:
	counter += 1
	test = data[i]
	query = """SELECT * FROM eanhotellist WHERE Name LIKE %s"""
	DB.execute(query, ("%"+i+"%",))
	row = DB.fetchone()
	if row == None:
		# print i
		# print test
		# failedmatches[i] = test
		# # print failedmatches
		fails += 1
	else:
		# for j in range(len(row)):
		# 	print "This is row "+str(j)+" "+str(row[j])
		# print test["link"]
		addquery =  """CuratedHotels (HotelID, EANHotelID, Name, City, StateProvince, Country, Location,
			ChainCodeID, RegionID, AvgRate, RegAvg, TripAdvisorRating, PulledAvgPrice, Website,
			LoyaltyProgram, StandardNightPoints, FifthNightFree, CashAndPointsPossible,
			CashOfCashAndPoints, PointsOfCashAndPoints, HighSeasonPossible, HighSeasonDates,
			HighSeasonPoints, PointSaverPossible, PointSaverDates, PointSaverPoints) VALUES (
			%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
			%s, %s, %s, %s"""
		DB.execute(query, (row[0], row[1], row[3], row[6], row[7], row[9], row[18], row[19], row[20], row[28],
			row[29], row[31],row[32], test["link"], test["loyalty"], test["category"], test["points"],
			test["fifthfree"], test["cashandpoints"], test["cashofcandp"], test["pointsofcandp"],
			test["highseasonapplies"], test["highseasondates"], test["highseasonrate"], 
			test["pointsaverapplies"], test["pointsaverdates"], test["pointsaverrate"]))
		CONN.commit()
		success += 1
	if success > 1:
		break
	else:
		continue

# print fails
# print success

# print "About to write to failed matches"

# f = open('failedmatches.json', 'w')

# f.write(json.dumps(failedmatches))

# print "I just wrote to failedmatches.json"