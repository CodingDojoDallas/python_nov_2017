#Assignment 3 Python.
#Multiples - Part 1. Printing Odd Numbers from 1 to 1000
for i in range(1,1001):
	if i % 2 != 0:
		print i

#Multiples - Part 2. Printing Numbers Multiples of 5 from 5 to 1.000.000
for i in range(1,1000001):
	if i % 5 == 0:
		print i

#Sum List. Program that sum every item in a list and prints the total.
a = [1, 2, 5, 10, 255, 3]
temp = 0
for x in a:
	temp = temp + x

print temp


#Average List. Sums all the items and the divides the total by the number of elements.
a = [1, 2, 5, 10, 255, 3]
temp = 0
for x in a:
	temp = temp + x

print temp/len(a)
