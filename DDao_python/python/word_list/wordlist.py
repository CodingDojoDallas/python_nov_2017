word_list = ['hello','world','my','name','is','Anna']
print [word for word in word_list if any(letter in word for letter in 'o')]