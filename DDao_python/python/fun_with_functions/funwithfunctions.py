for x in range(0, 11):
	if x%2 != 0:
		print "Number is", x, "This is an odd number."
	elif x%2 == 0:
		print "Number is", x, "This is an even number."



def multiply(arr,num):
	for i in range(len(arr)):
		arr[i] *= num
	return arr
i = [1,2,3,4,5]
b = multiply(i,5)
print b
