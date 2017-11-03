# def odd_even(arr):
# 	#loops as x many times, where x is the lenght of the arr, need the +1 to include the last value
# 	for x in range(1,arr+1):
# 		if x%2 == 0:
# 			print "Number is {}. This is an even number.".format(x)
# 		else:
# 			print "Number is {}. This is an odd number.".format(x)
# odd_even(2000)

def multiply(a, num):
	for x in range(0,len(a)):
		a[x] *= num
	return a
print multiply([1,2,3],5)
# 		#appends the value of x into the empty array, new_a
# 		new_a.append(x)	
# 	print a
# 	#after leaving the for loop x becomes the last index times 5
# 	print x
# 	print new_a

# multiply([1,2,3],5)

def layered_multiples(arr):
	new_arr = []
	for x in arr:
		new_arr1 = []
		for y in range(0, x):
			new_arr1.append(1)
		new_arr.append(new_arr1)
	return new_arr
x = layered_multiples(multiply([1,2,3],2))
print x
