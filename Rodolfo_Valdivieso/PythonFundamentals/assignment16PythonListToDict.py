#Assignment 16 Python - List to Dictionary
#unction that takes in two lists and creates a 
#single dictionary where the first list contains keys and the second values

print "Part1:"
print "------"
name            = ["Anna" , "Eli", "Pariece", "Brendan", "Amy"  , "Shane"   , "Oscar"]
favorite_animal = ["horse", "cat", "spider" , "giraffe", "ticks", "dolphins", "llamas"]

def makingDictionaries(a, b):
	newDictionary = {}
	for i in range(0,len(a)):
		newDictionary[a[i]]=b[i]

	return newDictionary

print makingDictionaries(name, favorite_animal)




name            = ["Anna" , "Eli", "Pariece", "Brendan", "Amy"  ]
favorite_animal = ["horse", "cat", "spider" , "giraffe", "ticks", "dolphins"         ]


print "Part2:"
print "------"

def makingDictionaries2(a, b):
	newDictionary2 = {}

	if len(a) > len(b):
		for i in range(0,len(a)):
			if i < len(b):
				newDictionary2[a[i]]=b[i]
			else:
				newDictionary2[a[i]]=""

	else:
		for i in range(0,len(b)):
			if i < len(a):
				newDictionary2[b[i]]=a[i]
			else:
				newDictionary2[b[i]]=""

	return newDictionary2

print makingDictionaries2(name, favorite_animal)

