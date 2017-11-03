def oddeven():
	for i in range(1,2001):
		if i%2==1:
			print("number is "+str(i)+". This is an odd number.")
		else:
			print("number is "+str(i)+". This is an even number.")
	return

oddeven()

def multiply(mylist,amp):
	newlist = []
	for element in mylist:
		newlist.append(element*amp)
	return newlist

a=[2,4,10,16]
b=multiply(a,5)
print b

def layered_multiples(arr):
	new_array=[]
	num=0
	for element in arr:
		num=element
		row=[]
		for i in range(0,num):
			row.append(1)
		new_array.append(row)
	return new_array
x = layered_multiples(multiply([2,4,5],3))
print x




