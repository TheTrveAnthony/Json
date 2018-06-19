"coding utf-8"

import json

class persoo:

	def __init__(self, k):

		with open("test.json") as f:	
			data = json.load(f)		# toutes les données récupérées d'un json sont sous forme de string
			
			self.nom = data["gens"][k]["nom"]
			self.age = int(data["gens"][k]["age"])
			self.ville = data["gens"][k]["ville"]




	#def presente(self):

	#	print("Je suis {0}, j'ai {1} ans et j'habite à {2}".format(self.nom, self.age, self.ville) )

	def __str__(self):

		return "Je suis {}, j'ai {} ans et j'habite à {}".format(self.nom, self.age, self.ville)


	def __getattr__(self, x):

		 #print("cette classe ne contient pas de {}.".format(x))
		print("lpij\n")
		x = self.nom
		print(x)

	def bday(self): # anniv

		self.age += 1

	def demenage(self, dest):

		self.ville = dest




class temps:

	def __init__(self, h, min, sec):

		self.s = sec
		self.m = min
		self.h = h

	def __str__(self):

		return "{}:{}:{}".format(self.h, self.m, self.s)

	def __add__(self, d):

		nd = temps(self.h, self.m, self.s)

		nd.h += d.h
		nd.m += d.m
		nd.s += d.s

		if nd.s >= 60:

			nd.m += 1
			nd.s = nd.s % 60

		if nd.m >= 60:

			nd.h += 1
			nd.m = nd.m % 60

		return nd


def strbool(x):

	if x == "True":

		return True

	elif x == "False":

		return False

	else:

		print("conversion impossible.\n")
	
