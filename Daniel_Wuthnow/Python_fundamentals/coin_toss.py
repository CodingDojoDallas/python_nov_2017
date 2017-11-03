import random

# print toss

def function():
	heads = 0
	tails = 0
	for x in range(1,5001):
		toss = round(random.random())+1
		#toss = 1
		#heads = 0
		#toss = 2
		#tails = 0
		if toss == 1:
			heads += 1
			print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(x,heads,tails)
		else:
			tails += 1
			print "Attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far".format(x,heads,tails)
	print "Ending the program, thank you!"
function()				