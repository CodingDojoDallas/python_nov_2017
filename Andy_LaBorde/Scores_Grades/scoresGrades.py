#generate 10 scores between 60 and 100 and
#assign grades 60-69: D, 70-79: C, 80-89: B, 90-100: A

# def grades()\
import random
for i in range(0, 10):
	random_num = random.randint(60, 100)
	if random_num <= 69:
		print "Score: {}; Your grade is D".format(random_num)
	if random_num > 69 and random_num < 80:
		print "Score: {}; Your grade is C".format(random_num) 
	if random_num > 79 and random_num < 90:
		print "Score: {}; Your grade is B".format(random_num) 
	if random_num > 89 and random_num < 101:
		print "Score: {}; Your grade is A".format(random_num) 