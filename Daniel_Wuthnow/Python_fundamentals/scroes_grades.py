def grades():
	
	for x in range(0,11):
		import random
		grade = round(random.random()*40)+60

		if grade >= 60 and grade < 70:
			print "Score: {}; Your grade is D".format(grade)
		elif grade >= 70 and grade < 80:
			print "Score: {}; Your grade is C".format(grade)
		elif grade >= 80 and grade < 90:
			print "Score: {}; Your grade is B".format(grade)
		elif grade >= 90 and grade <= 100:
			print "Score: {}; Your grade is A".format(grade)
	print "End of the program. Bye!"
grades()