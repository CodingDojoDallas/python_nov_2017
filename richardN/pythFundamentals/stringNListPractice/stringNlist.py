# Find & Replace
string = "It's thanksgiving day. It's my birthday too!"
print string.find("day")
string = string.replace("day","month")
print string
#ask why 18 keeps printing

#min & max
x = [2,54,-2,7,12,99,0,78,12,1]
print max(x)
print min(x)

#first & last
x = ["hello",2,54,-2,7,12,99,"world"]
print x[0], x[len(x)-1]

#new list
x = [12,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
first_list = x[:len(x)/2]
second_list = x[:len(x)/2]
print "first_list"
print "second_list"
second_list.insert(0,first_list)
print second_list
