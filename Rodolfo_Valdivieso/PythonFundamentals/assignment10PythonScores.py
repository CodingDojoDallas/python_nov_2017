#Assignment 10 Python Scores and Grades
#function that generates ten scores between 60 and 100
import random

def grades():
	for i in range(1, 11):
		score = random.randint(60,100)

		if (score <= 69):
			print "Score: ", score , " Your grade is D"
		elif (score >= 70 and score <= 79):
			print "Score: ", score , " Your grade is C"
		elif (score >= 80 and score <= 89):
			print "Score: ", score , " Your grade is B"
		else:
			print "Score: ", score , " Your grade is A"

	print "End of the program. Bye!"

grades()
