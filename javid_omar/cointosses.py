def cointoss():
	import random
	numhead=0
	numtail=0
	for i in range(1,5001):
		if random.randint(0,1):
			numtail+=1
			print "Attempt #"+str(i)+": Throwing a coin... It's a tail! ... Got "+str(numhead)+" head(s) so far and "+str(numtail)+" tail(s) so far"
		else:
			numhead+=1
			print "Attempt #"+str(i)+": Throwing a coin... It's a head! ... Got "+str(numhead)+" head(s) so far and "+str(numtail)+" tail(s) so far"
		
	return
cointoss()