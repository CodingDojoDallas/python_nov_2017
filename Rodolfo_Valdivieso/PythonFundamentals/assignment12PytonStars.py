#Assignment 12 Python - Stars
#Part 1 - Create a function called draw_stars() that takes a list of numbers and prints out *.
def draw_stars(a):
	for x in a:
		print "*" * x
print "Part 1:"
draw_stars([1, 2, 3, 4, 5])

#Part 2 - Allow a list containing integers and strings to be passed to the draw_stars() function.
# When a string is passed, instead of displaying *, display the first letter of the string according 
#to the example below. You may use the .lower() string method for this part.
def draw_starsPart2(a):
	for x in a:
		if type(x) is int:
			print "*" * x
		else:
			print x[0] * len(x)
print "Part 2:"
draw_starsPart2([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])