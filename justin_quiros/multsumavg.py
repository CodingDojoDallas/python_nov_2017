# printing all odd integers from 1 to 1000
#for x in range(1, 1000, 2):
#	print x
# printing all multiples of 5 from 5 to 1Mil
#for y in range(5, 1000000, 5):
#	print y

# printing the sum of variable a
arr = [1,2,5,10,255,3]
sum = 0

for a in range(0, len(arr)):
	sum += arr[a]

print sum


avg = 0

for a in range(0, len(arr)):
	avg = sum / len(arr)

print avg
