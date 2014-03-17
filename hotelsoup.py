from bs4 import BeautifulSoup
import requests
import re
import json

Hotel_dictionary = {}

for i in range(1,8):
	print "Hyatt category "+str(i)
	r  = requests.get("http://www.hyatt.com/gp/en/awards/hyatt_category_display.jsp?category="+str(i)+"&section=standard")
	point_list = [0,5000,8000,12000,15000,20000,25000,30000]
	data = r.text
	soup = BeautifulSoup(data)
	links_div = soup.findAll('div', attrs={'class':'hbGpInfoColumn hbGpClmn32'})
	for div in links_div:
		links = div.findAll('a')
		for a in links:
			# print a.contents[0]
			try:
				hotel = a.contents[0]
				Hotel_dictionary[hotel] = {}
				Hotel_dictionary[hotel]["link"] = a["href"]
				Hotel_dictionary[hotel]["loyalty"] = "Hyatt"
				Hotel_dictionary[hotel]["category"] = i
				Hotel_dictionary[hotel]["points"] = point_list[i]
				Hotel_dictionary[hotel]["fifthfree"] = False
				Hotel_dictionary[hotel]["cashandpoints"] = False
				Hotel_dictionary[hotel]["cashofcandp"] = None
				Hotel_dictionary[hotel]["pointsofcandp"] = None
				Hotel_dictionary[hotel]["highseasonapplies"] = False
				Hotel_dictionary[hotel]["highseasonrate"] = point_list[i]
				Hotel_dictionary[hotel]["highseasondates"] = None
				Hotel_dictionary[hotel]["weekendrateapplies"] = False
				Hotel_dictionary[hotel]["weekendpointrate"] = point_list[i]
				Hotel_dictionary[hotel]["pointsaverapplies"] = False
				Hotel_dictionary[hotel]["pointsaverdates"] = False
				Hotel_dictionary[hotel]["pointsaverrate"] = point_list[i]
			except:
				print "Add manually "+a.contents[0]

Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"] = {}
Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["link"] = "http://www.jeddah.park.hyatt.com/en/hotel/home.html"
Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["loyalty"] = "Hyatt"
Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["category"] = 5
Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["points"] = 20000
Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["fifthfree"] = False
Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["cashandpoints"] = False
Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["cashofcandp"] = None
Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["pointsofcandp"] = None
Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["highseasonapplies"] = False
Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["highseasonrate"] = 20000
Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["highseasondates"] = None
Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["pointsaverapplies"] = False
Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["pointsaverdates"] = False
Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["pointsaverrate"] = point_list[i]

print "Added manually Park Hyatt Jeddah - Marina, Club and Spa"


print "Hyatt is done"

for i in range(1,8):
	print "Adding Starwood Category "+str(i)
	r  = requests.get("http://www.starwoodhotels.com/preferredguest/account/starpoints/categories/popup.html?spgCategoryCode="+str(i))
	point_list = [0,3000,4000,7000,10000,12000,20000,30000]
	high_season_points_list = [0,3000,4000,7000,10000,16000,25000,35000]
	cashofcandp_list = [0, 30, 35, 55, 75, 100, 180, 275]
	pointsofcandp_list = [0, 1500, 2000, 3500, 5000, 6000, 10000, 15000]
	weekeendpoint_list = [0,2000,3000,7000,10000,12000,20000,30000]
	if i <= 2:
		weekendpossible = True
	else:
		weekendpossible = False
	if i >= 5:
		highseasonpossible = True
	else:
		highseasonpossible = False
	data = r.text
	soup = BeautifulSoup(data)
	table_row = soup.findAll('tr')
	for row in table_row:
		links = row.findAll('a')
		for a in links:
			# print a.contents[0]
			try:
				hotel = a.contents[0]
				Hotel_dictionary[hotel] = {}
				jslink = a["href"]
				jslink = re.search("location.href='(.*)'; }", jslink)
				jslink = jslink.group(1)
				Hotel_dictionary[hotel]["link"] = "http://www.starwoodhotels.com"+jslink	
				Hotel_dictionary[hotel]["loyalty"] = "Starwood"
				Hotel_dictionary[hotel]["category"] = i
				Hotel_dictionary[hotel]["points"] = point_list[i]
				Hotel_dictionary[hotel]["fifthfree"] = True
				Hotel_dictionary[hotel]["cashandpoints"] = True
				Hotel_dictionary[hotel]["cashofcandp"] = cashofcandp_list[i]
				Hotel_dictionary[hotel]["pointsofcandp"] = pointsofcandp_list[i]
				Hotel_dictionary[hotel]["highseasonapplies"] = highseasonpossible
				if highseasonpossible == True:
					highseasondates = []
					season_div = row.findAll('div', attrs={'id':'seasonInfo'})
					for div in season_div:
						highdivs = div.findAll('div')
						for date in highdivs:
							highseasondates.append(date.contents[0].encode('latin-1'))
					Hotel_dictionary[hotel]["highseasondates"] = highseasondates
					highseasondates = []
				Hotel_dictionary[hotel]["highseasonrate"] = high_season_points_list[i]
				Hotel_dictionary[hotel]["weekendrateapplies"] = weekendpossible
				Hotel_dictionary[hotel]["weekendpointrate"] = weekeendpoint_list[i]
				Hotel_dictionary[hotel]["pointsaverapplies"] = False
				Hotel_dictionary[hotel]["pointsaverdates"] = False
				Hotel_dictionary[hotel]["pointsaverrate"] = point_list[i]
			except:
				print "Add manually "+a.contents[0]

hotel = "Aloft Chennai OMR - IT Expressway"
Hotel_dictionary[hotel] = {}
Hotel_dictionary[hotel]["link"] = "http://www.starwoodhotels.com/alofthotels/property/overview/index.html?propertyID=3276"
Hotel_dictionary[hotel]["loyalty"] = "Starwood"
Hotel_dictionary[hotel]["category"] = 1
Hotel_dictionary[hotel]["points"] = 3000
Hotel_dictionary[hotel]["fifthfree"] = True
Hotel_dictionary[hotel]["cashandpoints"] = True
Hotel_dictionary[hotel]["cashofcandp"] = 30
Hotel_dictionary[hotel]["pointsofcandp"] = 1500
Hotel_dictionary[hotel]["highseasonapplies"] = False
Hotel_dictionary[hotel]["highseasonrate"] = 3000
Hotel_dictionary[hotel]["highseasondates"] = None
Hotel_dictionary[hotel]["weekendrateapplies"] = True
Hotel_dictionary[hotel]["weekendpointrate"] = 2000
Hotel_dictionary[hotel]["pointsaverapplies"] = False
Hotel_dictionary[hotel]["pointsaverdates"] = False
Hotel_dictionary[hotel]["pointsaverrate"] = 3000
print "added manually "+hotel

hotel = "Aloft Oklahoma City Downtown - Bricktown"
Hotel_dictionary[hotel] = {}
Hotel_dictionary[hotel]["link"] = "http://www.starwoodhotels.com/alofthotels/property/overview/index.html?propertyID=3623"
Hotel_dictionary[hotel]["loyalty"] = "Starwood"
Hotel_dictionary[hotel]["category"] = 4
Hotel_dictionary[hotel]["points"] = 10000
Hotel_dictionary[hotel]["fifthfree"] = True
Hotel_dictionary[hotel]["cashandpoints"] = True
Hotel_dictionary[hotel]["cashofcandp"] = 75
Hotel_dictionary[hotel]["pointsofcandp"] = 5000
Hotel_dictionary[hotel]["highseasonapplies"] = False
Hotel_dictionary[hotel]["highseasonrate"] = 10000
Hotel_dictionary[hotel]["highseasondates"] = None
Hotel_dictionary[hotel]["weekendrateapplies"] = False
Hotel_dictionary[hotel]["weekendpointrate"] = 10000
Hotel_dictionary[hotel]["pointsaverapplies"] = False
Hotel_dictionary[hotel]["pointsaverdates"] = False
Hotel_dictionary[hotel]["pointsaverrate"] = 10000
print "added manually "+hotel

print "Starwood is done"

for i in range(1,15):
	print "Processing Marriott Category " + str(i)
	f  = open("marriott/marriotcat"+str(i))
	data = f.read()
	f.close
	point_list = [0,7500,10000,15000,20000,25000,30000,35000,40000,45000,30000,40000,50000,60000,70000]
	pointsaver_list = [0,6000,7500,10000,15000,20000,25000,30000,35000,40000,20000,30000,40000,50000,60000]
	# data = r.text
	soup = BeautifulSoup(data)
	all_links = soup.findAll("a", attrs={"class": "sendto-link"})
	for a in all_links:
		hotel = a.contents[0]
		hotel = hotel.strip()
		Hotel_dictionary[hotel] = {}
		Hotel_dictionary[hotel]["link"] = "marriott.com"+a["href"]
		Hotel_dictionary[hotel]["loyalty"] = "Marriott"
		Hotel_dictionary[hotel]["category"] = i
		Hotel_dictionary[hotel]["points"] = point_list[i]
		Hotel_dictionary[hotel]["fifthfree"] = True
		Hotel_dictionary[hotel]["cashandpoints"] = False
		Hotel_dictionary[hotel]["cashofcandp"] = None
		Hotel_dictionary[hotel]["pointsofcandp"] = None
		Hotel_dictionary[hotel]["highseasonapplies"] = None
		Hotel_dictionary[hotel]["highseasonrate"] = point_list[i]
		Hotel_dictionary[hotel]["highseasondates"] = None
		Hotel_dictionary[hotel]["weekendrateapplies"] = False
		Hotel_dictionary[hotel]["weekendpointrate"] = point_list[i]
		Hotel_dictionary[hotel]["pointsaverapplies"] = True
		Hotel_dictionary[hotel]["pointsaverdates"] = None
		Hotel_dictionary[hotel]["pointsaverrate"] = pointsaver_list[i]

print "Marriott is done"

for i in range(1,11):
	print "Processing Hilton Category"+str(i)
	point_list = [0, 5000, 10000, 20000, 20000, 30000, 30000, 30000, 40000, 50000, 70000]
	high_point_list = [0, 5000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 95000]
	category = str(i)
	if i >= 4:
		high = True
	else:
		high = False
	pages_in_cat = [0, 3, 9, 24, 128, 66, 26, 14, 7, 4, 1]
	for j in range(0,pages_in_cat[i]):
		pagenum = str(j*15)	
		r  = requests.get("http://hhonors.hilton.com/en/hhonors/rewards/search_result_reward_levels.jhtml?%2Fcom%2Fhilton%2Fhotel%2FHotelSearchForm.city=&_D%3A%2Fcom%2Fhilton%2Fhotel%2FHotelSearchForm.city=+&%2Fcom%2Fhilton%2Fhotel%2FHotelSearchForm.state=&_D%3A%2Fcom%2Fhilton%2Fhotel%2FHotelSearchForm.state=+&country=&%2Fcom%2Fhilton%2Fhotel%2FHotelSearchForm.country=&_D%3A%2Fcom%2Fhilton%2Fhotel%2FHotelSearchForm.country=+&pageNum="+pagenum+"&sortOrder=&useVicinity=no&hhonorsRewardLevel="+category+"&hhonorsRewardCategory=1&_DARGS=%2Fen%2Fhotels%2Fsearch%2Fresults_body_hhonors_reward_levels.jhtml")
		data = r.text
		soup = BeautifulSoup(data)
		links = soup.findAll('a')
		for a in links:
			try:
				if "hotelname" in str(a.contents[0]):
					hotel_name = a.contents[0]
					hotel_name = re.search("""<font class="hotelname">(.*)</font>""", str(hotel_name))
					hotel_name = hotel_name.group(1)
					if hotel_name:	
						hotel = hotel_name.encode('latin-1')
						hotel = hotel.replace("&amp;", "&")
						Hotel_dictionary[hotel] = {}
						Hotel_dictionary[hotel]["link"] = "http://hhonors3.hilton.com/en/index.html"
				 		Hotel_dictionary[hotel]["loyalty"] = "Hilton"
						Hotel_dictionary[hotel]["category"] = i
						Hotel_dictionary[hotel]["points"] = point_list[i]
						Hotel_dictionary[hotel]["fifthfree"] = True
						Hotel_dictionary[hotel]["cashandpoints"] = False
						Hotel_dictionary[hotel]["cashofcandp"] = None
						Hotel_dictionary[hotel]["pointsofcandp"] = None
					 	Hotel_dictionary[hotel]["highseasonapplies"] = high
						Hotel_dictionary[hotel]["highseasonrate"] = high_point_list[i]
						Hotel_dictionary[hotel]["highseasondates"] = "Viewable on Booking"
						Hotel_dictionary[hotel]["weekendrateapplies"] = False
						Hotel_dictionary[hotel]["weekendpointrate"] = point_list[i]
						Hotel_dictionary[hotel]["pointsaverapplies"] = False
						Hotel_dictionary[hotel]["pointsaverdates"] = False
# 						Hotel_dictionary[hotel]["pointsaverrate"] = point_list[i]

			except:
				pass

print "Hilton is done"
print "About to write to json"

f = open('hoteldictionary.json', 'w')

f.write(json.dumps(Hotel_dictionary))

print "Let's open our json and see if that worked!"