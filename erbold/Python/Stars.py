# Task1 - Create a function called draw_stars() that takes a list of numbers and prints out *.

# #input:

# x=[4,6,1,3]

# #outputs:

# ****
# ******
# *
# ***

# Logic:

# -Given a list of numbers
# -Take each number within the list and print out that many *

# Pseudocode:

# Take index position 0
# Get the value within the index position
# Use the value as the range for a new array
# Print a * within each index position
# repeat for each index position of the original list

def stars(bank):


	for x in bank:

		print "*" * x


stars([4,6,1,3])	


# Task2 - Modify the function above so that draw_stars() takes a list containing integers and 
#strings, then outputs the first letter of the string for each letter when there's an string.

# #inputs:

# x=[4,"Tom", 1, "Michael", 5,7,"Jimmy Smith"]

# #outputs:

# ****
# ttt
# *
# mmmmmmm
# *****
# etc...

def stars(bank):


	for x in bank:

		if isinstance(x, int):
			print "*" * x
		elif isinstance(x, str):
			length=len(x)
			letter=x[0].lower()
			print letter * length

x=[4,"Tom", 1, "Michael", 5,7,"Jimmy Smith"]
stars(x)	