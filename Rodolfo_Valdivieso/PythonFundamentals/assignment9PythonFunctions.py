#Assignment 9 Python Fundamentals.
#Create a function called odd_even that counts from 1 to 2000
def odd_even():
	for i in range(1,21):
		if (i % 2 == 0):
			print "Number is ", i , ". This is an even number."
		else:
			print "Number is ", i , ". This is an odd number."


odd_even()

#Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) 
#and returns a list where each value has been multiplied by 5.

def multiply(listA, number):
	listB = []
	for x in listA:
		listB.append(x*number)

	return listB

print multiply([2, 4, 10, 16], 5)

#Hacker Challenge.
#function that takes the multiply function call as an argument. 
#Your new function should return the multiplied list as a two-dimensional list.

def layered_multiples(arr):
	new_array = []
	temp_arr = []
	for x in arr:
		for i in range(1, (x+1)):
			temp_arr.append(1)
			
		new_array.append(temp_arr)
		temp_arr = []
		
	return new_array

x = layered_multiples(multiply([2,4,5],3))
print x