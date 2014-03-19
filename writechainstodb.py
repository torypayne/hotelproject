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
		print i
		print test
		failedmatches[i] = test
		# print failedmatches
		fails += 1
	else:
		# print row
		success += 1
	if counter > 10:
		break
	else:
		continue

# print fails
# print success

print failedmatches