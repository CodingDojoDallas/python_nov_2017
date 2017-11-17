# part 2Modify MathDojo to take at least one integer(s) and/or list(s) 
#as a parameter with any number of values passed into the list

class  MathDojo(object):
	def __init__(self):
		self.result = 0

	def add(self,*num):
		for i in num:
			if isinstance(i,int):
				self.result+=i
			elif isinstance(i,list):
				for j in i:
					self.result+=j
		return self

	def subtract(self,*num):
		for i in num:
			if isinstance(i,int):
				self.result-=i
			elif isinstance(i,list):
				for j in i:
					self.result -=j
		return self

md=MathDojo()
print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result

