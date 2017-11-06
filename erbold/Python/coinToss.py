#Inputs: 
# #the number of times flipping a coin
# #the heads or tails option for the coin flip

# Outputs:
# -the number of the attempt
# -how many times we get tails
# -how many times we get heads

# Logic:
# -name the function
# -inputs/Outputs
# -print/returned w/o if or loops
# -define the variables (the pieces that are changing)
# -convert our code into condensed code 

# Logic1:

# import random

# def coint_toss():
# 	print "Starting the program..."
# 	numAttempt=1

# 	while(numAttempt<21):
# 		head_or_tail="heads"
# 			if random.choice()<.5
# 				head_or_tail="tails"
# 	# 	print "Attemp #", numAttempt, ": Throwing a coin... It's a ", head_or_tail, "! ..." 	

# coint_toss()

#print "Attemp #", numAttempt, ": Throwing a coin... It's a ", head_or_tail, "! ..." 	


import random

def coint_toss(yup):
	numAttempt=1
	tail_count=0
	head_count=0	

	for x in range(1,yup):
		head_or_tail=''

		new_toss=random.randint(0,1)
		if new_toss==1:
			head_count += 1
			head_or_tail="head(s)"
			print "Attemp #", numAttempt, ": Throwing a coin... It's a ", head_or_tail, "! Got", head_count, "head(s) so far and", tail_count, "tail(s) so far." 	
		else:
			tail_count += 1
			head_or_tail="tail(s)"
			print "Attemp #", numAttempt, ": Throwing a coin... It's a ", head_or_tail, "! Got", head_count, "head(s) so far and", tail_count, "tail(s) so far." 	
		numAttempt+=1
coint_toss(5001)

