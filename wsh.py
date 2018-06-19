"coding utf-8"

import json
#import perso

noms = []
viles = []
ages = []

with open("test.json") as f:

	data = json.load(f)
	#print(data)

	
	for i, val in enumerate(data["gens"]):
		#noms.append(data["gens"][i]["nom"])
		print"{}:{}".format(i, val)

#print(noms)

