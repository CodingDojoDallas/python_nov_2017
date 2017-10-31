bio = {"name": "Justin", 
		"age": 27,
		"country of birth": "The United States",
		"favorite language": "Python"}

#print bio["name"]

def info():
	for key in bio:
		#bio[key] ---> look at it as if the key to the
		#dictionary unlocks the value, and that is what
		#is displayed 
		print "My",key, "is", bio[key]
info()