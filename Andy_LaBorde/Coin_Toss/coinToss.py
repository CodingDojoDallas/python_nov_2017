import random
attempt = 0
head = 0
tail = 0
for i in range(0, 5000):

	
	coin = random.randint(1,2)
	if coin == 1:
		attempt += 1
		head += 1
	 	print "Attempt #{}: Trowing a coin... Its a head!! ... Got {} head(s) so far and {} tail(s) so far".format(attempt, head, tail)
	elif coin == 2:
	 	attempt += 1
	 	tail += 1
	 	print"Attempt #{}: Trowing a coin ... Its a Tails!! ... got {} head(s) so far and {} tail(s) so far".format(attempt, head, tail)