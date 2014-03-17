import os
import MySQLdb

# connect
# dbpw = os.environ.get('SUDOPW')


db = MySQLdb.connect(host="localhost", user="root", passwd="",
 db="hotelchains")

cursor = db.cursor()

# execute SQL select statement
result = cursor.execute("select * from ratetesting")

print result

# # commit your changes
# db.commit()

# # get the number of rows in the resultset
# numrows = int(cursor.rowcount)

# # get and display one row at a time.
# for x in range(0,numrows):
#     row = cursor.fetchone()
#     print row[0], "-->", row[1]