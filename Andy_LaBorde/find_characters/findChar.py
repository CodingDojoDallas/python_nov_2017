# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = []

for x in range(0, len(word_list)):
	if char in word_list[x]:
		new_list.append(word_list[x])
print new_list

