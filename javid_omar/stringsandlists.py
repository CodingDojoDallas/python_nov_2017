def findandreplace():
	words = "It's thanksgiving day. It's my birthday,too!"
	print words.find("day")
	wordsnew = words.replace("day", "month", 1)

def minandmax(nums):
	print('minimum is: ', min(nums))
	print('maximum is: ', max(nums))

def firstandlast(x):
	print(x[0])
	print(x[len(x)-1])
	newx = [x[0], x[len(x)-1]]
	return newx

def newlist(og):
	og.sort()
	first = og[:len(og)/2]
	second = og[len(og)/2:]
	second.insert(0,first)
	return second

	


