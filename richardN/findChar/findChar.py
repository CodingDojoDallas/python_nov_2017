# input
word_list = ['hello','world','my','name','is','Anna', "and", "what", "the", "fork"]
char = 'o'
# output
new_list = []


for i in word_list:
    if i.find("o") != -1:
        new_list.append(i)
print new_list
