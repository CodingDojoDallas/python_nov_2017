
#Part 1: Create a Python class called MathDojo that has the methods 
#add and subtract. Have these 2 functions take at least 1 parameter.

class MathDojo(object):
	def __init__(self):
		self.result =0

	def add(self,*num):
		for i in num:
			self.result+=i
		return self

	def subtract(self,*num):
		for i in num:
			self.result-=i
		return self

md=MathDojo()
print "Result:",md.add(2).add(2,5).subtract(3,2).result

