words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')
print words.replace('day', 'month')

x = [2,54,-2,7,12,98]

print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]

print x[0], x[len(x)-1]

y=[]
y.append(x[0]+ x[len(x)-1])
print y


x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x

newList = x[:6]
x=x[5:]
x[0]=newList

print x
