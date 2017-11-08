# Input:

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','milk']

# Output:

# -If both lists are identical print "The lists are the same"
# -If both lists are not identical then print "The lists are not the same"

# Logic:

# -Take two lists
# -Test if the value in each index position of list 1 is equal to the corresponding index position of list 2
# -If true then print "The..."
# -If not true then print "..."

# Pseudocode:

# -def compare(arr1, arr2)
# -if arr1[i]=arr2[i]
# -print "The lists are the same"
# -else print "..."
# -compare(list_one,list_two)

# Code:

def compare(arr1, arr2):

	for i in range(1):
		if arr1[i]==arr2[i] and len(arr1)==len(arr2) and arr2==arr1:
			print "The lists are the same"
		else: 
			print "The lists are not the same"
compare(list_one, list_two)  