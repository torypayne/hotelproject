from bs4 import BeautifulSoup
import requests
import re

Hotel_dictionary = {}

r  = requests.get("http://www.starwoodhotels.com/preferredguest/account/starpoints/categories/popup.html?spgCategoryCode=7")


for i in range(1,8):
	print i
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
				hotel = a.contents[0].encode('latin-1')
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
					highseasondates = None
				Hotel_dictionary[hotel]["highseasonrate"] = high_season_points_list[i]
				Hotel_dictionary[hotel]["weekendrateapplies"] = weekendpossible
				Hotel_dictionary[hotel]["weekendpointrate"] = weekeendpoint_list[i]
				Hotel_dictionary[hotel]["pointsaverapplies"] = False
				Hotel_dictionary[hotel]["pointsaverdates"] = False
				Hotel_dictionary[hotel]["pointsaverrate"] = point_list[i]
			except:
				print "Add manually "+a.contents[0]

# print Hotel_dictionary