# Assignment 11 Python - Coin Tosses
#function that simulates tossing a coin 5,000 times. 
#function should print how many times the head/tail appears.
import random
def coinTosses(a):
	tail=0
	head=0
	for i in range(1,a+1):
		x_rounded = round(random.random())
		if (x_rounded == 1):
			tail = tail + 1
			print "Attempt #",i,": Throwing a coin... It's a tail! ... Got ",head," head(s) so far and ",tail," tail(s) so far"
		else:
			head = head + 1
			print "Attempt #",i,": Throwing a coin... It's a head! ... Got ",head," head(s) so far and ",tail," tail(s) so far"

	print "Ending the program, thank you!"

attemps=100
coinTosses(attemps)