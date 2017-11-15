#Create function that counts to 2000 exectuing and odd/even paramater

def odd_even():
	for num in range(1,2001):
		if num %2 == 1:
			print "The Number is "+ str(num) +". This is an odd number."
			
		elif num %2 ==0:
			print "The Number is "+ str(num) +". This is an even number."
odd_even()


#create a function	that iterates though an array and multiplies each int by 5

def multiply(arr,b):
		
	for i in range(0,len(arr)):
		arr[i] *= b
	return arr

multiply([2,4,5,6],5)

# Write a function that takes the multiply function call as an argument. 
#Your new function should return the multiplied list as a two-dimensional list. 
#Each internal list should contain the 1's times the number in the original list.

def layered_multiples(arr):
	print arr
	new_arr=[]
	for i in arr:
		n_arr = []
		for n in range(0,i):
			n_arr.append(1)
		new_arr.append(n_arr)
	return new_arr

x = layered_multiples(multiply([2,4,5],3))
print x
