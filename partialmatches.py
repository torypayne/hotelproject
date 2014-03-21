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

json_data=open('matchednameissues.json')

data = json.load(json_data)

counter = 0


for i in data:
	counter += 1
	test = data[i]
	query = """SELECT * FROM eanhotellist WHERE Name LIKE %s"""
	DB.execute(query, ("%"+i+"%",))
	row = DB.fetchone()
	print i
	print test
	print row
	if counter >=1:
		break