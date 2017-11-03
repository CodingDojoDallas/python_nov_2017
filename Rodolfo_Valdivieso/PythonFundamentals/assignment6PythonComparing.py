list_one = [0,1,2]
list_two = [0,1,2]

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','milk']


different = False

if len(list_one) != len(list_two):
	print "The lists are not the same."
	different = True
else:
	for x in range(0,len(list_one)):
		if list_one[x] != list_two[x]:
			different = True

	if different is True:
		print "The lists are not the same."
	else:
		print "The lists are equal."

