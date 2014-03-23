import json
from pprint import pprint
import MySQLdb

DB = None
CONN = None

json_data=open('matchednameissues.json')
data = json.load(json_data)

def connect_to_db():
	global DB
	global CONN
	CONN = MySQLdb.connect(host="localhost", user="root", passwd="", db="hotelchains")
	DB = CONN.cursor()
	print DB

#For loop that iterates through all hotels in data
#Check if a hotel is in curated hotels already
#If so delete it
#If not, look it up in EAN hotel list
#Try to add it to DB
#Print command we just tried
#If it failed, wait for next command
#If command = check, check if it's in the DB
#If command = next, go to start of for loop again


def check_curated(name):
	query = """SELECT * FROM CuratedHotels WHERE Name LIKE %s"""
	DB.execute(query, ("%"+name+"%",))
	row = DB.fetchone()
	if row != None:
		print name +" is already in curated"
		return True
	else:
		print name +" isn't in curated yet"
		return False

def check_on_id(HotelID):
	query = """SELECT * FROM CuratedHotels WHERE HotelID = %s"""
	DB.execute(query, (HotelID,))
	row = DB.fetchone()
	if row != None:
		print name +" is already in curated"
		return True
	else:
		print row
		return False

def pull_row_from_ean(name):
	query = """SELECT * FROM eanhotellist WHERE Name LIKE %s"""
	DB.execute(query, ("%"+name+"%",))
	row = DB.fetchone()
	return row

def try_to_add_hotel(name, row):
	test = data[name]
	location = str(row[18])
	location = location.replace("(","")
	location = location.replace(")","")
	try:
		test["highseasondates"]
	except:
		test["highseasondates"] = None
	highseason = "Dates not available"
	try:
		addquery =  """INSERT INTO CuratedHotels (HotelID, EANHotelID, Name, City, StateProvince, Country, Location,
			ChainCodeID, RegionID, AvgRate, RegAvg, TripAdvisorRating, PulledAvgPrice, Website,
			LoyaltyProgram, LoyaltyCategory, StandardNightPoints, FifthNightFree, CashAndPointsPossible,
			CashOfCashAndPoints, PointsOfCashAndPoints, HighSeasonPossible, HighSeasonDates,
			HighSeasonPoints, PointSaverPossible, PointSaverDates, PointSaverPoints) VALUES (
			%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
			%s, %s, %s, %s)"""
		DB.execute(addquery, (row[0], row[1], row[3], row[6], row[7], row[9], location, row[19], row[20], row[28],
			row[29], row[31],row[32], test["link"], test["loyalty"], test["category"], test["points"],
			test["fifthfree"], test["cashandpoints"], test["cashofcandp"], test["pointsofcandp"],
			test["highseasonapplies"], highseason, test["highseasonrate"], 
			test["pointsaverapplies"], test["pointsaverdates"], test["pointsaverrate"]))
		print name + " just got added"
		CONN.commit()
		pass
	except:
		print "You need to manually add "+name
		print DB._last_executed
		print """INSERT INTO CuratedHotels (HotelID, EANHotelID, Name, City, StateProvince, Country, Location,
			ChainCodeID, RegionID, AvgRate, RegAvg, TripAdvisorRating, PulledAvgPrice, Website,
			LoyaltyProgram, LoyaltyCategory, StandardNightPoints, FifthNightFree, CashAndPointsPossible,
			CashOfCashAndPoints, PointsOfCashAndPoints, HighSeasonPossible, HighSeasonDates,
			HighSeasonPoints, PointSaverPossible, PointSaverDates, PointSaverPoints) VALUES ("""
		print row[0], row[1], row[3], row[6], row[7], row[9], location, row[19], row[20], row[28], row[29], row[31],row[32], test["link"], test["loyalty"], test["category"], test["points"], test["fifthfree"], test["cashandpoints"], test["cashofcandp"], test["pointsofcandp"], test["highseasonapplies"], highseason, test["highseasonrate"], test["pointsaverapplies"], test["pointsaverdates"], test["pointsaverrate"]
		return raw_input("next to go to the next, check to check again")



def main():
    connect_to_db()
    command = None
    while command != "quit":
        print "quit to quit, next for next, check to check a hotel again"
        command = raw_input("Partial match review> ")
        for name in data:
        	check = check_curated(name)
        	if check == True:
        		continue
        	else:
        		row = pull_row_from_ean(name)
        		command = try_to_add_hotel(name, row)
        		while command == "check":
        			check_curated(name)
        			try_to_add_hotel(name, row)
        		continue



    CONN.close()

if __name__ == "__main__":
    main()