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
partialsuccess = 0

failedmatches = {}
matchednamewithissues = {}


for i in data:
	counter += 1
	test = data[i]
	query = """SELECT * FROM eanhotellist WHERE Name LIKE %s"""
	DB.execute(query, ("%"+i+"%",))
	row = DB.fetchone()
	if row == None:
		# print i
		print i + " didn't work"
		failedmatches[i] = test
		# # print failedmatches
		fails += 1
	else:
		try:
			addquery =  """INSERT INTO CuratedHotels (HotelID, EANHotelID, Name, City, StateProvince, Country, Location,
				ChainCodeID, RegionID, AvgRate, RegAvg, TripAdvisorRating, PulledAvgPrice, Website,
				LoyaltyProgram, LoyaltyCategory, StandardNightPoints, FifthNightFree, CashAndPointsPossible,
				CashOfCashAndPoints, PointsOfCashAndPoints, HighSeasonPossible, HighSeasonDates,
				HighSeasonPoints, PointSaverPossible, PointSaverDates, PointSaverPoints) VALUES (
				%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
				%s, %s, %s, %s)"""
			DB.execute(addquery, (row[0], row[1], row[3], row[6], row[7], row[9], row[18], row[19], row[20], row[28],
				row[29], row[31],row[32], test["link"], test["loyalty"], test["category"], test["points"],
				test["fifthfree"], test["cashandpoints"], test["cashofcandp"], test["pointsofcandp"],
				test["highseasonapplies"], test["highseasondates"], test["highseasonrate"], 
				test["pointsaverapplies"], test["pointsaverdates"], test["pointsaverrate"]))
			print i + " just got added"
			success += 1
		except:
			print i + " sort of worked"
			matchednamewithissues[i] = test
			partialsuccess += 1


CONN.commit()
print "fails: "+str(fails)
print "successes: "+str(success)
print "partial successes "+str(partialsuccess)

print "About to write to failed matches"

f = open('failedmatches.json', 'w')

f.write(json.dumps(failedmatches))

print "I just wrote to failedmatches.json"

j = open('matchednameissues.json', 'w')

f.write(json.dumps(matchednamewithissues))

print "I just wrote to matchednameissues.json"