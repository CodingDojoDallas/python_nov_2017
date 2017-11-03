# for x in xrange(1,1000,2):
# 	print x

#do not use (var)range. only use range 
# for i in range(5,1000000,5):
# 	print i

# arr = [1,2,3,4,5]
# sum = 0
# #y is the index of the array, len(arr) is just the lenght of the array
# for y in range(0,len(arr)):
# 	#adds the value at arr at index y to the sum
# 	sum = sum + arr[y]
	
# print sum

arr = [1,2,3,4]
sum = 0
avg = 0
for x in xrange(0,len(arr)):
	sum = sum + arr[x]
	avg = sum / len(arr)
print avg
