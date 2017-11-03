def compare(list_one,list_two):
	if len(list_one)!=len(list_two):
		print "The lists are not the same"
		return
	for i in range(0,len(list_one)):
		if list_one[i]!=list_two[i]:
			print "The lists are not the same"
			break
		elif i==(len(list_one)-1):
			print "The lists are the same."


list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

compare(list_one,list_two)