
# Inputs:

# -Random number generator producing 10 random numbers
# -The grading table

# Score:60-69;Grade-D
# Score:70-79;Grade-C
# Score:80-89;Grade-B
# Score:90-100;Grade-A

# Outputs:

# Scores and Grades
# Score: 87; Your grade is B
# Score: 67; Your grade is D
# Score: 95; Your grade is A
# Score: 100; Your grade is A
# Score: 75; Your grade is C
# Score: 90; Your grade is A
# Score: 89; Your grade is B
# Score: 72; Your grade is C
# Score: 60; Your grade is D
# Score: 98; Your grade is A
# End of the program. Bye!

# Logic:

# -Generate 10 random numbers between 60-100
# -Take the first number generated, display It
# -Then check which range the number falls in
# -Display the letter grade corresponding to that range
# -Repeat ten times

# Pseudocode:

# def grades(totalnum)
# 	print "Scores and Grades"
# 	while num is <= totalnum 
# 		score=random.randint(60-100)
# 		grade=if score in certain range then return that corresponding letter
# 		print "Score: ", score, "; Your grade is ", grade
# 	print "End of the program. Bye!"
# grades(10)

# code:

import random

def grades(students):
	print "Scores and Grades"
	num=0
	while num <= students:
		score=random.randint(60,100)
		if score >=60 and score <= 69:
			print "Score: ", score, "; Your grade is D"
		elif score >=70 and score <=79:
			print "Score: ", score, "; Your grade is C"
		elif score >=80 and score <=89:
			print "Score: ", score, "; Your grade is B"
		elif score >=90 and score <=100:
			print "Score: ", score, "; Your grade is A"
		num+=1
	print "End of the program. Bye!"

grades(10)


