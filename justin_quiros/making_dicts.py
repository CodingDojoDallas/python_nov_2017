name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

# def make_dict(arr1, arr2):
# 	new_dict1 = zip(arr1, arr2)
# 	new_dict2 = dict(new_dict1)
# 	print new_dict2
# make_dict(name, favorite_animal)

def make_unequal_dict(arr1, arr2):
	if len(arr1)>=len(arr2):
		#zip() will move two lists into 1 like a zipper
		new_dict1 = zip(arr1, arr2)
		#dict() will form the zip() into a real dictionary
		new_dict2 = dict(new_dict1)
	else:
		len(arr1) < len(arr2)
		new_dict1 = zip(arr2, arr1)
		new_dict2 = dict(new_dict1)
	print new_dict2
make_unequal_dict(name, favorite_animal)