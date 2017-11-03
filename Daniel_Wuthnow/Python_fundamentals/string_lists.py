# words = "It's thanksgiving day. It's my birthday,too!"
# print words.find("day")
# #.replaces(what i am replacing, what will be replacing the first index)
# print words.replace("day", "month")

# x = [1,324,6,3,-8,6]
# #min and max are called and in the () is what is looked through to find the value wanted
# print min(x)
# print max(x)

# x = ["hello",2,54,-2,7,12,98,"world"]
# #prints the first index of x
# print x[0]
# #prints the last value of x. x[-2] would be the second to last index
# print x[-1]
# #makes array with the first value in the first index and the last value into the seconed index
# z = [x[0],x[-1]]
# print z

arr = [19,2,54,-2,7,12,98,32,10,-3,6]
arr = sorted(arr)
print arr
#the second half of the arr
arr2 = arr[len(arr)/2:]
#the first half of the arr
arr3 = arr[:len(arr)/2]
print arr2
print arr3
#in arr2 this function inserts arr3 into index 0 sliding over the other index
arr2.insert(0,arr3)
print arr2
