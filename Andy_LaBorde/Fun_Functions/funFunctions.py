def odd_even():
	for number in range(1, 2001):

		if number % 2 == 0:
			print "The number is {}. This is an Even number".format(number)
		else:
			print "The number is {}. This is an odd number".format(number)
odd_even()

# print result

def multiply(arr, num):
	for x in range(0, len(arr)):
		arr[x] *= num
	return arr
numbers_array = [3,6,8,10,67]

print multiply(numbers_array, 5)
		
multiply([1,3,5,7,9],5)

def layered_multiples(arr):
	print arr
	new_arr = []
	for x in arr:
		val_arr = []
		for i in range(0,x):
			val_arr.append(1)
		new_arr.append(val_arr)
	return new_arr

x = layered_multiples(multiply([2,4,5],3))
print x
		


