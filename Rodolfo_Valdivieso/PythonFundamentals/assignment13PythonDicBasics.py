#Assignment 13 Pythob - Dictionary Basics
#dictionary containing some information about yourself. 
#The keys should include name, age, country of birth, favorite language.

dictionary = {'name':'Rodolfo','age':32,'country of birth':'Venezuela','favorite language':'Python'}


def assignment(d):
	for x in d:
		print "My ",x ," is ", d[x]

assignment(dictionary)