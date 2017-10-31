list_one = [1,2,5,6,2]
list_two = [2,2,5,6,2]
count = 0

if len(list_one) != len(list_two):
	print "The lists are not the same."

for x in range(0, len(list_two)):
	if list_one[x] != list_two[x]:
		print "The lists are not the same."
		count += 1
if count == 0:
	print "The lists are the same."
