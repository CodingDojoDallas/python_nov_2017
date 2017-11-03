arr = ['magical unicorns',19,'hello',98.98,'world']
sum = 0
new_string = ""
count_str = 0
count_int = 0
firstStr = False
strChecked = False
for x in arr:
	y = isinstance(x,str)
	z = isinstance(x,int)
	a = isinstance(x,float)
	if z == True or a == True:
		sum = sum + x
		count_int += 1
	elif y == True:
		#checks to see if the string is the first string in the array. if it is it wont add the space. if you dont do this it will mess up the charactor count
		if firstStr == False:
			new_string += x
			firstStr = True
			strChecked = True
		else:
			new_string = new_string +" "+ x
			count_str += 1
if count_str > 0 and count_int > 0:
	print "The list you entered is of mixed type"
elif count_str > 0 and count_int == 0:
	print "The list you entered is of string type"
elif count_str == 0 and count_int > 0:
	print "The list you entered is of integer type"

print "Sum: {}".format(sum)
print "String: {}".format(new_string)
