from bs4 import BeautifulSoup
import requests

Hotel_dictionary = {}

for i in range(1,8):
	print i
	r  = requests.get("http://www.starwoodhotels.com/preferredguest/account/starpoints/categories/popup.html?spgCategoryCode="+str(i))
	point_list = [0,3000,4000,7000,10000,12000,20000,30000]
	high_season_points_list = [0,3000,4000,7000,10000,16000,25000,35000]
	cashofcandp_list =
	pointsofcandp_list = 
	data = r.text
	soup = BeautifulSoup(data)
	links_div = soup.findAll('div', attrs={'class':'hbGpInfoColumn hbGpClmn32'})
	for div in links_div:
		links = div.findAll('a')
		for a in links:
			# print a.contents[0]
			try:
				hotel = a.contents[0].encode('latin-1')
				Hotel_dictionary[hotel] = {}
				Hotel_dictionary[hotel]["link"] = a["href"]
				Hotel_dictionary[hotel]["loyalty"] = "Hyatt"
				Hotel_dictionary[hotel]["category"] = i
				Hotel_dictionary[hotel]["points"] = point_list[i]
				Hotel_dictionary[hotel]["fifthfree"] = False
				Hotel_dictionary[hotel]["cashandpoints"] = False
				Hotel_dictionary[hotel]["cashofcandp"] = None
				Hotel_dictionary[hotel]["pointsofcandp"] = None
				Hotel_dictionary[hotel]["highseasonrate"] = point_list[i]
				Hotel_dictionary[hotel]["highseasondates"] = None
				Hotel_dictionary[hotel]["weekendrateapplies"] = False
				Hotel_dictionary[hotel]["weekendpointrate"] = point_list[i]
			except:
				print "Add manually "+a.contents[0]