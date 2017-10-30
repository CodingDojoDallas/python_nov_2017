# take a list and determine each element in the ksit by type. 
#for int, add to running sum
# for string, push to new string.

l = ['magical unicorns',19,'hello',98.98,'world']
sum = 0
newStr ="String:"
numcheck = False
strcheck = False



for x in range (0,len(l)):
	if type(l[x]) == int:
		sum += l[x]
		numcheck = True
	elif type(l[x]) == str:
		newStr= newStr + ' '+l[x]
		strcheck=True

if numcheck == True and strcheck==True:
	print "The list you entered is of mixed type"
	print sum
	print newStr
elif numcheck==False and strcheck==True:
	print "The list you entered is of string type"
	print newStr
else:
	print "The list you entered is of integer type"
	print sum



