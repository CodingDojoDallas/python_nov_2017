#Compare two lists and print a message based on the results

list_one = [1,2,5,6,2,16]
list_two = [1,2,5,6,2]

if set(list_one) == set(list_two):
	print 'the lists are the same'
else:
	print 'the lists are not the same'
