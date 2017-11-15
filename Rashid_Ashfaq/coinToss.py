import random 
def coinToss():
	head = 0;
	tail = 0;
	count =0;

	for i in range(1, 5001): 
		toss = round(random.random())
		if toss == 0:
			head += 1
			count += 1
			print "Attempt #", count , ": Throwing a coin... It's a head! ... Got " , head , "head(s) so far and " , tail , "tail(s) so far"
		else: 
			tail += 1
			count += 1
			print "Attempt #",count , ": Throwing a coin... It's a tail! ... Got " , head , "head(s) so far and " , tail , "tail(s) so far"

coinToss()
