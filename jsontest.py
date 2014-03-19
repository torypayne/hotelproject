import json
from pprint import pprint

# test = {"hello":"world"}

# f = open('hoteldictionary.json', 'w')

# f.write(json.dumps(test))

json_data=open('hoteldictionary.json')

data = json.load(json_data)
# pprint(data)
# pprint(data["Aloft Abu Dhabi"])

counter = 0
for i in data.iteritems():
	counter += 1

print counter

json_data.close()