'''
Tuple 
- container for a fixed sequence of data objects.
- sequences, just like lists

tuples are IMMUTABLE, cannot be changed

lists are defined with square brackets, tuples use parentheses

For example'''
tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5 )
tuple_letters = "a", "b", "c", "d"

'''
useful for representing records

if you try to modify an element, we get an error, because tuples are immutable (like strings)
once python createst a tuple in memory, it cannot be changed
    - we can add and slice tuples though
'''

dog = dog + ("domestic",)
#result is...
#("Canis Familiaris", "Dog", "carnivore", 12, "domestic")
dog = dog[:3] + ("man's best friend",) + dog[4:]
#result is...
#("Canis Familiaris", "Dog", "carnivore", "man's best friend", "domestic")

'''
Built in Functions
len(sequence): returns length of tuple
max(seq): returns largest value
sum(seq): returns sum of all values
enumerate(seq): used in for loop context to return two item tuple for each item in list
    - indicates index followed by value at that index
map(function, seq): applies function to every item in sequence. returns list of results
min(seq): returns lowest value
sorted(seq): returns a sorted sequence

Returning Tuples:
    - good way to return multiple values, grouped together

Why?
    - less flexible than lists, but can be good thing depending on use case
    - grouped info that consumers of code can't modify, that should be kept constant



