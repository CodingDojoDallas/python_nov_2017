'''
A dictionary is a mutable set type, can store any number of python objects, including other set types
    - pairs (items) of keys and values
    - also called associative arrays or hash tables

- unordered collection of objects
- values accessed using a key
- can shrink or grow as needed
- contents can be modified
- can be nested
- sequence operations like slice can't be used with dictionaries (b/c unordered?)

Creating Dictionaries
- lists[], tuples(), dictionaries{}
'''
weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
'''
weekend created using literal notation. the key-value pairs were enclosed by {}. Pairs separated by commas, .
captials created with empty dictionary, then adding the key:value s.

Accessing Values
- use square brackets along with key to obtain value
'''#Iterating Dictionaries
user = {'first_name': 'Michael',
        'last_name': 'JOrdan'}

print user['first_name']
#'Michael'

for key in user:     //'first_name'
    print key       //'last_name'
#'first_name'
#'last_name'

for key in user:
    print user[key]
#'Michael'
#'Jordan'

for key,val in user.iteritems():
    print val
#'Michael'
#'Jordan'

'''Functions/Methods
cmp(dict1, dict2) - compares 2 dicts. Lengths, key names, values
    - returrns 0 if both dicts equal, -1 if dict1 > dict2, 1 if dict1 < dict2

len() - total length of dictionary
str() - produces string representation of dict
type() - returns the type of passed variable. Will return 'dictionary' type of var is dict

python methods
dict.method(yourDict) or yourDict.method()

.clear() - removes all elements from dict
.copy() - returns shallow copy dictionary
.fromkeys(sequence, [value]) - creates new dict with keys from seq and values set to value
.get(key, default=None) - returns value or default if key is not in dictionary
.has_key(key) - returns true if key available in dict, otherwise false
.items() - returns list of dict's (key,value) tuple pairs
.keys() - return a list of dictionary keys
.setdefault(key, default=None) - similar to get(), but sets dict[key]=default if key not already in dict
.update(dict2) - adds dict2's key-value pairs to an existing dict1
.values() - returns list of dict values
zip() - two lists "zipped" together into list of tuples (2-tuple list form)
    - dict() will transform into real dict
    - superfluous elements will not be used (whether extra keys or extra values) in zip()


