import random
random_num = random.random()*100

def grade(num):
	if num <60:
		print "Score:", num, "; Your grade is F"
	elif num <= 69 and num >= 60:
		print "Score:", num, "; Your grade is D"
	elif num <= 79 and num >= 70:
		print "Score:", num, "; Your grade is C"
	elif num <= 89 and num >= 80:
		print "Score:", num, "; Your grade is B"
	elif num <= 100 and num >= 90:
		print "Score:", num, "; Your grade is A"

grade(random_num)