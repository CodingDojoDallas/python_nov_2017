
import random

#def coinToss():
heads=0
tails=0
count=0
for i in range(1,5001):

	coin =random.randint(1,2)
	if coin == 1:
		count+=1
		heads+=1
		print "Attempt #"+str(count)+": Throwing a coin...it's Heads! Got "+str(heads)+" heads so far and "+str(tails)+" tails so far."
	elif coin == 2:
		count+=1
		tails+=1
		print "Attempt #"+str(count)+": Throwing a coin...it's Tails! Got "+str(heads)+" heads so far and "+str(tails)+" tails so far."
#return coinToss()