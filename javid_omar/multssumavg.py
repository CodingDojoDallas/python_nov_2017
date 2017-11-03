def multiples1():
	for count in range(1,1000): #starts us at 1 and ends at 999
		if (count%2==1):  #checks if count is odd and should be printed
			print count
multiples1()

def multiples2():
	for count in range(5, 1000001):	#starts our loop at 5 and goes to 1000000
		if (count%5==0):	#prints if count is a multiple of 5
			print count
multiples2()

def sum():
	total = 0	#values will be added to this variable to get the sum
	a = [1,2,5,10,255,3]
	for val in a:	#spans the list a
		total+=val 	#adds to sum
	print total
sum()

def avg():
	total = 0		#will hold the sum
	a = [1,2,5,10,255,3]
	for val in a:		#spans the list a
		total+=val
	average = total/len(a)		#divides the sum by number of elements 
	print average
avg()
