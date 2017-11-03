#Assignment 15 Python - Tuples
# function that takes in a dictionary and returns
# a list of tuples where the first tuple item is the key and the second is the value

# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def tuples(dictionary):
	listOfTuples =[]
	tupleX = ()
	for keys in dictionary:
		#create the tuple
		tupleX = tupleX + (keys,)
		tupleX = tupleX + (dictionary[keys],)
		listOfTuples.append(tupleX)
		tupleX = ()
	return listOfTuples

print tuples(my_dict)
