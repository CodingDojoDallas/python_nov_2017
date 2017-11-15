import random 
print "Score and Grades"
def gradeScore():
	for i in range(1,11):
		score = random.randint(0,101)
		if 60<=score<=69:
			print "Score:" ,+ score  ,"Your grade is D"
		elif 70<=score<=79:
			print "Score:" , +score ,"Your grade is C"
		elif 80<=score<=89:
			print "Score:" , + score , "Your grase is B"
		elif 90<=score<=100:
			print "Score:", + score ,"Your grate is A"
		elif score<60:
			print "Score:", + score ,"Your grade is F"
	print "End of the program. Bye!"	

gradeScore()