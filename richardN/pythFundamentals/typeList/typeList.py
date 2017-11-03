#input
mixedList = ['magical unicorns',19,'hello',98.98,'world']
numList = [2,3,1,7,4,12]
strngList = ['magical','unicorns']

def identMixType(lst):
    newList = ''
    total = 0
    intger = 0
    string = 0

    for value in (lst):
        if isinstance(value, int) or isinstance (value, float):
            total += value
            intger = 1
        else:
            newList += value + " "
            string = 1


    if intger == 1 and string == 1:
        print "the array you entered is a mixed type"
    elif intger==0 and string==1:
        print "the array is just a string"
    else:
        print "the array is just numbers"
    print "string:" + newList
    print "total:", (sum(numList))

identMixType (strngList)


'''
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"

#output
"The list you entered is of integer type"
"Sum: 29"

#output
"The list you entered is of string type"
"String: magical unicorns"
'''
