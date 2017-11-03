'''Making Dictionaries'''
# create function, takes in 2 lists, creates single dict
# first list contains keys, second values
# lists will be equal length

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "test1", "test2"]

def make_dict(arr1, arr2):
    new_dict = {}

    '''Hacker Challenge with unequal list lengths'''
    if len(arr2) > len(arr1): 
        longerList = arr2
        shorterList = arr1
    else:
        longerList = arr1 #1st list default key (longer) list
        shorterList = arr2

    diff = len(longerList) - len(shorterList)
    for i in range(diff):
        shorterList.append(None) #make shorter list as long as longer list, filled with None

    for x in range(len(longerList)):
        new_dict[longerList[x]] = shorterList[x]
    return new_dict

print make_dict(name, favorite_animal)