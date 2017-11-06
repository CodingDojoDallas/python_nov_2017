# Input= [1,2000]

# Output=[Number is 1. This is an odd number.]...



# Take a number range from 1 to 2000,
# then Print each number out
# 	within the printed number identify whether its an odd or even number
a=range(1,90)
def odd_even(a):


	for x in a:
		if x%2==0:
			print "Number is ", x,". This is an even number."
		else:
			print "Number is ", x,". This is an odd number."

odd_even(a)

# input: a=[2,4,10,16]

# output: a=[10,20,50,80]


# Given a list
# 	Multiply each value within the list by 5
# 	Then print the new list 


# a=[2,4,10,16]

# def Multiply(a):

# 	for x in range(len(a)):	
# 		print a[x]*5

# Multiply(a)

multiples=[2,4,5]

def layered_multiples(arr):
	print arr
	new_array=[]
	for x in arr:
		val_arr=[]
		for i in range(0,x):
			val_arr.append(1)
		new_array.append(val_arr)
	return new_array

x = layeredMultiples(multiply([2,4,5],3))
print x 