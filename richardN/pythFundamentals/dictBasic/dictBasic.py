me = {'name':'richard','ethn': 'asian','car': 'mini','mOt': 'bike','age':25}

#
# def print_dictionary_values(me):
#     for item in me:
#         print me['age']

# print_dictionary_values(me)

print me['name']
print me.keys() # calls for the keys
print len(me) # asks for the number of keys
print str(me) #gives dictionary as a string
print type(me) # informs you what kind of variable it is..... ie: tuple, int, float, string, etc...
# .clear() it "clears" the dictionary
#print me.copy() shallow copy? WTfrack
print me.items()
print me.values()
