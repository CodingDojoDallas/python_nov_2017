def multiply(mylist,num):
	for i in range(len(mylist)):
		 mylist[i] *= num
	return mylist
a =[2,4,10,16]		 
b = multiply(a,5)
print b
