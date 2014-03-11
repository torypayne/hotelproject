# sudo mysql hotelchains


Hotel_Chains = ["Starwood", "Hilton", "Hyatt", "Marriott"]

Starwood_Hotels = ["W Hotel", "Westin", "Sheraton", "Le Meridien", "St Regis", "Luxury Collection", "Four Points", "aLoft", "element"]

Hilton_Hotels = ["Waldorf-Astoria", "Conrad", "Hilton", "DoubleTree", "Embassy Suites", "Hilton Garden Inn", "Hampton Inn", "Home2 Suites by Hilton", "Homewood Suites", "Hilton Grand Vacations"]

Hyatt_Hotels = ["Park Hyatt", "Andaz", "Grand Hyatt", "Hyatt", "Hyatt Regency", "Hyatt Place", "Hyatt House", "Hyatt Residence Club", "Zilara", "Ziva", "mLife"]

Marriott_Hotels = ["Ritz-Carlton", "Bulgari", "JW Marriott", "Edition", "Autograph Collection", "Renaissance", "AC by Marriott", "Gaylord", "Courtyard", "Springhill Suites", "Fairfield Inn", "Residence Inn", "Townplace Suites", "Marriott Executive Apartments", "marriottvacationclub", "JW Marriott"]

# for i in range(len(Starwood_Hotels)):
# 	Starwood_Hotels[i] = "'%"+Starwood_Hotels[i]+"%'"
# 	print "update hotelchains set loyaltyprogram = 'Starwood' where chainname like "+Starwood_Hotels[i]+";"

for i in range(len(Hilton_Hotels)):
	Hilton_Hotels[i] = "'%"+Hilton_Hotels[i]+"%'"
	print "update hotelchains set loyaltyprogram = 'Hilton' where chainname like "+Hilton_Hotels[i]+";"

for i in range(len(Hyatt_Hotels)):
	Hyatt_Hotels[i] = "'%"+Hyatt_Hotels[i]+"%'"
	print "update hotelchains set loyaltyprogram = 'Hyatt' where chainname like "+Hyatt_Hotels[i]+";"

for i in range(len(Marriott_Hotels)):
	Marriott_Hotels[i] = "'%"+Marriott_Hotels[i]+"%'"
	print "update hotelchains set loyaltyprogram = 'Marriott' where chainname like "+Marriott_Hotels[i]+";"
