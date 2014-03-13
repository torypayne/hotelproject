from bs4 import BeautifulSoup
import requests

Hotel_dictionary = {}

for i in range(1,2):
	print i
	r  = requests.get("http://hhonors.hilton.com/en/hhonors/rewards/search_result_reward_levels.jhtml?%2Fcom%2Fhilton%2Fhotel%2FHotelSearchForm.city=&_D%3A%2Fcom%2Fhilton%2Fhotel%2FHotelSearchForm.city=+&%2Fcom%2Fhilton%2Fhotel%2FHotelSearchForm.state=&_D%3A%2Fcom%2Fhilton%2Fhotel%2FHotelSearchForm.state=+&country=&%2Fcom%2Fhilton%2Fhotel%2FHotelSearchForm.country=&_D%3A%2Fcom%2Fhilton%2Fhotel%2FHotelSearchForm.country=+&pageNum=0&sortOrder=&useVicinity=no&hhonorsRewardLevel="+str(i)+"&hhonorsRewardCategory=1&_DARGS=%2Fen%2Fhotels%2Fsearch%2Fresults_body_hhonors_reward_levels.jhtml")
	data = r.text
	soup = BeautifulSoup(data)
	howmany_span = soup.findAll('span', attrs={'style':'Arial, Helvetica, sans-serif; font-size: 12px; font-weight: bold; color: #FFFFFF;'})
	for span in howmany_span:
		print "found one"