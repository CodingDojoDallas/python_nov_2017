def typelist(l):
	string = ""
	total = 0
	totaltype = ""
	for element in l:
		if isinstance(element, float) or isinstance(element, int):
			total+=element
		if isinstance(element, str):
			string+=element+" "
	for i in range(1,len(l)):
		if type(l[i])==type(i-1]):
			if isinstance(l[i], float):
				totaltype = "float"
			if isinstance(l[i], int):
				totaltype = "integer"
			if isinstance(l[i], str):
				totaltype = "string"
		else:
			totaltype = "mixed"
			break
	


	print "Sum: "+total
	print "String: "+string
	print "The list you entered is of " + totaltype + " type"