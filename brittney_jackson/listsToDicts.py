# create a function that atkes in two lists and creates a single dictionary

def makeDict(arr1, arr2):
	
	newDict= zip(arr1, arr2)

	

	print newDict

makeDict(['name', 'age', 'dob', 'gender'], ['Bee', '30', '6/3/87', 'F'])