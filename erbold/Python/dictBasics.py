
# input: 

# My name
# Erbold
# My age
# 56
# My country of birth
# Mongolia
# My favorite language
# Python

# output:

# My name is Erbold
# My age is 56
# My country of birth is Mongolia
# My favorite language is Python

# Logic:

# -create a dictionary
# -populate that dictionary with (my name, my age, my country of birth, my favorite language)
# and populate each category accordingly
# -create a function that will output certain categories that i want and their values


# Pseudocode:

# -create.dictionary(mydict)
# -mydict{
# My name is: Erbold
# My age is: 56
# My country of birth: Mongolia
# My favorite language is: Python
# }
# -func dictValues(info)

# 	for dictValues:
# 		if index values equals [0,3,4]
# 		print info[]

# dictValues()

#Actual code:

mydict={"nam":"myoho","baby":"diapers","language":"Python"}
# "My name is":"Erbold"

# "My country of birth is ":The United States
# "My favorite language is ":Python
# newdict=[n for n in mydict]
print mydict


def newdictname(mydict):
	for a, b in mydict.iteritems():
		print "My", a, "is", b

newdictname (mydict)



