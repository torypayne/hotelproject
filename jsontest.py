import json

test = {"hello":"world"}

f = open('hoteldictionary.json', 'w')

f.write(json.dumps(test))
