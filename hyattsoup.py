from bs4 import BeautifulSoup
import requests

Hotel_dictionary = {}

for i in range(1,8):
	print i
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

# Testing showed that "Park Hyatt Jeddah – Marina, Club and Spa" was the only item that needed 
# to be added manually
# Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"] = {}
# Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["link"] = a["href"]
# Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["loyalty"] = "Hyatt"
# Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["category"] = i
# Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["points"] = point_list[i]
# Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["fifthfree"] = False
# Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["cashandpoints"] = False
# Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["cashofcandp"] = None
# Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["pointsofcandp"] = None
# Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["highseasonrate"] = point_list[i]
# Hotel_dictionary["Park Hyatt Jeddah - Marina, Club and Spa"]["highseasondates"] = None


