#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"
sum = 0
string = 'String:'
numcheck = False
strcheck = False


for x in range(0, len(l)):
	if type(l[x]) == int:
		sum += l[x]
		numcheck = True
	elif type(l[x]) == str:
		# if l[x] == l[0]:
		string = string + ' ' + l[x]
		strcheck =True
if numcheck == True and strcheck == True:
	print "the type of list you entered is of the mixed type"
	print sum
	print string
elif numcheck == False and strcheck == True:
	print "The type of list you entered is of the string type"
	print string
else:
	print "The type of list you entered is of the integer type"
	print sum

# print sum
# print string
