name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
# print name_animal
# print name_animal_dict
# def make_dict(arr1, arr2):
#   new_dict = {}
# name_animal = zip(name, favorite_animal)
# name_animal_dict = dict(name_animal)
#   # return new_dict
# print name_animal_dict
# make_dict(name, favorite_animal)

#hacker challange
def make_better_dict(arr1, arr2):
	if len(arr1) >= len(arr2):
		new_dict1 = zip(arr1, arr2)
		new_dict2 = dict(new_dict1)
	else:
		new_dict1 = zip(arr2, arr1)
		new_dict2 = dict(new_dict1)
	print new_dict2


make_better_dict(name, favorite_animal)