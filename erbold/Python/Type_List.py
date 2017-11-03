my_list = ['magical unicorns',19,'hello',98.98,'world']
numblist = [2,3,1,7,4,12]
wording = ['magical','unicorns']



def identMixtype(lst):

	number = 0
	words = ""



	for value in lst:
		if isinstance(value, int) or isinstance(value, float):
			number += value
		elif isinstance(value, str):
			words += value

	if number and words:
		print "The array you entered is of mixed type"
		print "String", words
		print "Number", number
		print ""

	elif number:
		print "Only numbers"
		print "Sum:", number
		print ""
	else:
		print "Just words"
		print "String: ", words
		print ""


identMixtype(my_list)
identMixtype(numblist)
identMixtype(wording)