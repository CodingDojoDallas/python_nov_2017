name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def make_dict(arr1, arr2):
	new_dict = zip(name, favorite_animal)
	new_dict2 = dict(new_dict)
	print new_dict2


make_dict(name, favorite_animal)