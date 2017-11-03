def scoresngrades():
	import random
	print "Scores and Grades"
	grade=0
	for i in range(0,10):
		grade=random.randint(60,100)
		if grade>=60 and grade<=69:
			print "Score: "+str(grade)+"; Your grade is D"
		if grade>=70 and grade<=79:
			print "Score: "+str(grade)+"; Your grade is C"
		if grade>=80 and grade<=89:
			print "Score: "+str(grade)+"; Your grade is B"
		if grade>=90 and grade<=100:
			print "Score: "+str(grade)+"; Your grade is A"
	print "End of the program. Bye!"
	return


scoresngrades()


