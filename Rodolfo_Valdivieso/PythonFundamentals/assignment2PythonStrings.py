words = "It's thanksgiving day. It's my birthday,too!"
#Finds the Position of the first instance of word Day.
print words.find("day")

#Creating a new string and replacing the word Day with the word Month
words2 = words.replace("day","month")
print words
print words2

numbers = [2,54,-2,7,12,98]

#Printing the min and max values of a given array
print "The Min is: " , min(numbers)
print "The Max is: " , max(numbers)

#Print the first and last values of an array
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0] + " " + x[len(x) - 1]

#Creating a list
y=[]
y.append(x[0])
y.append(x[len(x) - 1])
print y

#Creating a second list and using loops.
x=[19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
y=[]
z=[]

for i in range(0,len(x)/2):
	y.append(x[i])

z.append(y)

for i in range((len(x)/2), len(x)):
	z.append(x[i])

print z 
	



