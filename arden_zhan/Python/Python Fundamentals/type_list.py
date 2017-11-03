# l = ['magical unicorns',19,'hello',98.98,'world']
# l = [2,3,1,7,4,12]
l = ['magical','unicorns']

newString = ""
sum = 0
strFirst = True

numCheck = False
strCheck = False

for item in l:
    if type(item) == str:
        if strFirst == True:
            newString += item
            strFirst = False
            strCheck = True
        else: newString = newString + " " + item
    if type(item) == int or type(item) == float:
        numCheck = True
        sum += item



if numCheck == True and strCheck == True: 
    print "The list you entered is of mixed type"
    print "String:", newString
    print "Sum:", sum
elif numCheck == True and strCheck == False:
    print "The list you entered if of integer type"
    print "Sum:", sum
elif numCheck == False and strCheck == True:
    print "The list you entered is of string type"
    print "String:", newString