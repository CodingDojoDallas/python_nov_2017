def odd_even():
	for x in range(1, 2001):
		if x % 2 == 0:
			print "Number is", x,"This is an even number."
		else:
			print "Number is", x,"This is an odd number."

odd_even()


def multiply(arr, num):
	for x in range(0, len(arr)):
		#print x
		arr[x] *= num
	return arr
print multiply([2,3,5,6], 5)


def layered_multiples(arr):
   	#print arr
   	new_arr1 = []
   	for x in arr:
   		print x
   		new_arr2 = []
   		#print new_arr2
   		for y in range(0, x):
   			new_arr2.append(1)
		new_arr1.append(new_arr2)
	return new_arr1
x = layered_multiples(multiply([2,4,5],3))
print x

