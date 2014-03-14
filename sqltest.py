import random

for i in range(16):
	highrate = str(random.randint(200,250))
	lowrate = str(random.randint(100,175))
	region = str(random.randint(1,3))
	print "Insert into ratetesting (HoteliestID, Hotelnamesies, HighestPossRate, LowestPossRate, RegCitCode) values ('"+str(i)+"','Hotel "+str(i)+"', '"+highrate+"', '"+lowrate+"', '"+region+"');"