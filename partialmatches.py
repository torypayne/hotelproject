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

#For loop that iterates through all hotels in data
#Check if a hotel is in curated hotels already
#If so delete it
#If not, look it up in EAN hotel list
#Try to add it to DB
#Print command we just tried
#If it failed, wait for next command
#If command = check, check if it's in the DB
#If command = next, go to start of for loop again



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


def main():
    connect_to_db()
    json_data=open('matchednameissues.json')
	data = json.load(json_data)
    command = None
    while command != "quit":
        print "quit to quit"
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split("||")
        print tokens
        command = tokens[0]
        args = tokens[1:]


    CONN.close()

if __name__ == "__main__":
    main()