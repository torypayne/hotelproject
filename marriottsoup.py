from bs4 import BeautifulSoup

Hotel_dictionary = {}

for i in range(1,15):
	print i
	f  = open("marriott/marriotcat"+str(i))
	data = f.read()
	f.close
	point_list = [0,7500,10000,15000,20000,25000,30000,35000,40000,45000,30000,40000,50000,60000,70000]
	pointsaver_list = [0,6000,7500,10000,15000,20000,25000,30000,35000,40000,20000,30000,40000,50000,60000]
	# data = r.text
	soup = BeautifulSoup(data)
	all_links = soup.findAll("a", attrs={"class": "sendto-link"})
	for a in all_links:
		hotel = a.contents[0].encode('latin-1')
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

print Hotel_dictionary