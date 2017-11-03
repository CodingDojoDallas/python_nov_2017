#Assignment: Type List.
#input

l = [2,3,1,7,4,12]
l = ['magical','unicorns']
l = ['magical unicorns',19,'hello',98.98,'world']

string = ""
sums   = 0.0
isInteger = 0 
isString = 0

for x in l:
	if (type(x) is int) or (type(x) is float):
		sums = sums + x
		isInteger=1

	elif type(x) is str:
		string = string +" "+ x
		isString=1

if (isString==1) and (isInteger==1):
	print "The list you entered is of mixed type"
	print "String:"+string[1:]
	print "Sum:", sums
elif (isString==0) and (isInteger==1):
	print "The list you entered is of integer type"
	print "Sum:", sums
else:
	print "The list you entered is of string type"
	print "String:"+string[1:]
