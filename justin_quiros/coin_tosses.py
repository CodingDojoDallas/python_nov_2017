import random
a = "heads"
b = "tails"
def cointoss():
	acount = 0
	bcount = 0
	for x in range(1,5001):
		y = random.randint(1,2)
		if y == 1:
			acount = acount + 1
			print "Attempt #", x, "Throwing a coin... It's a head! ... Got", acount, "heads( so far and", bcount, "tails(s) so far"
		else:
			bcount = bcount + 1
			print "Attempt #", x, "Throwing a coin... It's a a tail! ... Got", acount, "heads(s) so far and", bcount, "tails(s) so far"
	print "Ending the program, thank you!"
cointoss()
