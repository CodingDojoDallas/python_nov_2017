words = "It's thanksgiving day. It's my birthday, too!"

print words.find('day')

print words.replace('day', 'month')

x = [2,54,-2,7,12,98]

print min(x)
print max(x)

x = ["hello", 2,54,-2,7,12,98,"world"]
y =[]

# print x[0] , x[len(x)-1]
y.append(x[0])
y.append (x[len(x)-1])
print y

x = [19,2,54,-2,-7,12,98,32,10,-3,6]

x.sort()
print x

print x[:5]
print x[5:]
x = [x[:5]]+x[5:]
# print [x[:5]]+x[5:]
print x