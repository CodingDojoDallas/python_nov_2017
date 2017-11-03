list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','hats']
a = True

if len(list_one) != len(list_two):
	print "The lists are not the same."

for x in range(len(list_one)):
	if list_one[x] != list_two[x]:
		a = False

if a == True:
	print "The lists are the same."
else:
	print "The lists are not the same"