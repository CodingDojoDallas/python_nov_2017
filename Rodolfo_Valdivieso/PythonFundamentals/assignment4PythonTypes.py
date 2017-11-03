#Assignment: Filter by Type

x = 45
x = 100
x = 455
x = 0
x = -23
x = "Rubber baby buggy bumpers"
x = "Experience is simply the name we give our mistakes"
x = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
x = ""
x = [1,7,4,21]
x = [3,5,7,34,3,2,113,65,8,89]
x = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
x = []
x = ['name','address','phone number','social security number']


if type(x) is int:
	print "is integer"
	if x >= 100:
		print "that's a big number"
	else:
		print "small number"
elif type(x) is str:
	print "is string"
	if len(x) > 50:
		print "long sentence"
	else:
		print "short sentence"
elif type(x) is list:
	print "is a list"
	if len(x) > 10:
		print "Big List"
	else:
		print "short List"