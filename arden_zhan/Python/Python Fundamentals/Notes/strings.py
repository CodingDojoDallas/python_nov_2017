name = 4
print "My name is", name

#cannot concatenate 'str' and 'int' objects
#print "My name is " + name

#string interpolation. Use {} and .format() to inject vars into string
first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)

#outdated method of string interpolation
hw = "hello %s" % 'world'
print hw
# the output would be:
# hello world

#Built-In String Methods
x = "Hello World"
print x.upper()

#common string methods
'''
string.count(substring): returns number of occurrences of substring in string.

string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.

string.find(substring): returns the index of the start of the first occurrence of substring within string.

string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.

string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.

string.split(): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
'''