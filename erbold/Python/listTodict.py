# Input:

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

# Output:

# newDict={
# 	"Anna": "horse",
# 	"Eli": "cat"
# }

# The ask:

# I am to take two lists of equal length and create a new dictionary where the first list
# makes up the keys and the 2nd list makes up the values of my new dictionary. 

# The logic:

# -Create a new dictionary
# -Set the values of the first list "name" to be the keys for the dictionary
# -Then set the values of the 2nd list "favorite_animal" to be the values for the dictionary
# -Return the new dictionary/print whatever

# Pseudocode:

# -function newDict(arr1,arr2):
# 	dictionary={}
# 	for key in dictionary:
# 		key=arr1[i]
# 		dictionary.append[key]
# 	for value in dictionary:
# 		value=arr2[i]
# 		dictionary.append[value]
# 	print dictionary
# newDict(name, favorite_animal)

# Code:

def make_dict(arr1, arr2):
	new_dict={arr1[i]: arr2[i] for i in range(len(arr1))}
	print new_dict
make_dict(name, favorite_animal)

