def findcharacters(word_list, char):
	new_list = []
	for element in word_list:
		if element.find(char)!=-1:
			new_list.append(element)
	print "new_list = "+str(new_list)



a = ['hello','world','my','name','is','Anna']
b = 'o'

findcharacters(a,b)

