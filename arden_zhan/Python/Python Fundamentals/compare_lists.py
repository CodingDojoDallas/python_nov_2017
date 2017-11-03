#Compare Lists

# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]

# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

def compare(one, two):
    if len(one) != len(two): 
        print "The lists are not the same."
        return
    for x in range(len(one)): #range of len(one) = len(two)
        if one[x] != two[x]:
            print "The lists are not the same."
            return
    print "The lists are the same."

compare(list_one, list_two)
