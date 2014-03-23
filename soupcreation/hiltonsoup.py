from bs4 import BeautifulSoup
import requests
import re

Hotel_dictionary = {}

for i in range(1,11):
	print i
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
						Hotel_dictionary[hotel]["pointsaverrate"] = point_list[i]

			except:
				pass

print Hotel_dictionary
