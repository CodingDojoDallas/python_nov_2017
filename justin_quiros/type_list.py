arr = ['magical unicorns',19,'hello',98.98,'world']

sum = 0
new_str = ""
numstr = 0
numint = 0
stringequals = ""

for x in arr:
	y = isinstance(x, str)
	z = isinstance(x, int)
	a = isinstance(x, float)

	if z == True or a == True:
		sum = sum + x
		numint = numint + 1
	elif y == True:
		new_str = new_str + x + " "
		numstr = numstr + 1
	if numstr > 0 and numint > 0:
		stringequals = "String is mixed"
	if numstr > 0 and numint == 0:
		stringequals = "Strings only"
	if numstr == 0 and numint > 0:
		stringequals = "Integers only"

print new_str
print sum
print stringequals


