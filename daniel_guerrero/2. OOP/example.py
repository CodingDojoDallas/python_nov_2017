class MyNumber(object):
	def __init__(self,num=10):
		self.num = num

	def add1(self):
		self.num +=1

	def add(self, n):
		self.num += n


myNum = MyNumber(5)
myNum.add1()
myNum.add(3)
print myNum.num


#===============================================================
