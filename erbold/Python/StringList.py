# x=3
# y=2
# while y>0:
# 	print y
# 	y=y-1
# else:
# 	print "Nam Myoho Renge Kyo bitches!"

#Find and replace
words="It's thanksgiving day. It's my brithday, too!"
print words.find("day")

#Max
x=[2,56,218,-5,46]
print max(x)

#Min
x=[2,56,218,-5,46]
print min(x)

#First and Last
x=["yesss",45,-56,23,1,"Myoho"]
print(x[0],x[-1])

x=["yesss",45,-56,23,1,"Myoho"]
y=(x[0],x[-1])
print y


#New List
x=[19,2,54,-2,7,12,98,32,10,-3,6]
x=sorted(x)
print(x)
y=x[:len(x)/2]
z=x[len(x)/2:]
print y
print z
z.insert( 0, y)
print z
# arr2.insert[0,array3]
