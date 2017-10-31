#   str() built-in method changes int to str

for i in range (0,13):
	if i==0:
		output="x "
	else:
		output+= str(i)+" "
print output

for x in range(1,13):
	output=str(x)+" "
	for count in range(1,13):
		output+= str(x*count)+" "

	print output