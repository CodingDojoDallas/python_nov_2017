#Find and Replace
words = "It's thanksgiving day.  It's my birthday, too!"
print words.find("day")

#replaced day with the month
print words.replace("day", "month")

#Finding the min and max values of a string
x = [1,54,234,-11,35,99]
print min(x)
print max(x)

# Finding values within a variable using indicies 
y = ["hi", 12, 22, 95, "bye", 76]
print y[0]
# minus 1 gives you the last value in this variable
print y[-1]

# Created a new list with the first and last value of the original list
z = [y[0], y[-1]]
print z


arr1 = [19,2,54,-2,7,12,98,32,10,-3,6]
arr1 = sorted(arr1)
print arr1

arr2 = arr1[:len(arr1)/2]
print arr2

arr3 = arr1[len(arr1)/2:]
print arr3


arr3.insert(0, arr2)
print arr3







