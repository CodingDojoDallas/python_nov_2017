'''
String and List Practice
.find()
.replace()
min()
max()
.sort()
len()
'''

print "Find and Replace"
words = "It's thanksgiving day. It's my birthday, too!"
print "Position of first instance of day:", words.find("day")
print words.replace("day", "month", 1)

print ""
print "Min and Max"
x = [2,54,-2,7,12,98]
print "List:", x
print "Min value of list:", min(x)
print "Max value of list:", max(x)

print ""
print "First and Last"
x = ["hello",2,54,-2,7,12,98,"world"]
print "List:", x
newList = [x[0], x[len(x) - 1]]
print "List of first and last element:", newList

print ""
print "New List"
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print "Sorted List", x
half = len(x) / 2
firstHalf = x[:half]
secondHalf = x[half:len(x)]
print "First Half:", firstHalf
print "Second Half:", secondHalf
secondHalf.insert(0, firstHalf)
print "Output:", secondHalf