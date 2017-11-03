# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ""
for x in word_list:
	if char in x:
		new_list = new_list + x +" " 
print new_list