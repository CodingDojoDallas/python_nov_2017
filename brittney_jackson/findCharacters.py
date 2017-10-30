#

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
newList =[]

for x in range(0,len(word_list)):
	if char in word_list[x]:
		newList.append(word_list[x])

print newList
