# Print all odd numbers from 1-1000

for x in range(1,1001):
	if x%2 == 1:
		print x

# print multiples of 5 from 5 - 1,000,000
for x in range(5,1000000):
	if x%5 == 0:
		print x

# program to print sums of all values in the given list
a = [1,2,5,10,255,3]
print sum(a)

# program to average sums in the given list
a = [1,2,5,10,255,3]
print sum(a) / len(a)