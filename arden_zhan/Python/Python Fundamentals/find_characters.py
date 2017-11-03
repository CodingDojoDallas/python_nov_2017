#Find Characters
# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
# new_list = ['hello','world']

def find(words, char):
    new_list = []
    for x in range(len(words)):
        if char in words[x]: 
            new_list.append(words[x])
    return new_list

print find(word_list, char)