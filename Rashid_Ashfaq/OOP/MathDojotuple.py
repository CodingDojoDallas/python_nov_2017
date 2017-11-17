#Part 3 support Tuple
class  MathDojo(object):
	def __init__(self):
		self.result = 0

	def add(self,*num):
		for i in num:
			if isinstance(i,list):
				self.result+=i
			elif isinstance(i,tuple):
				for j in i:
					self.result+=j
		return self

	def subtract(self,*num):
		for i in num:
			if isinstance(i,list):
				self.result-=i
			elif isinstance(i,tuple):
				for j in i:
					self.result -=j
		return self

md=MathDojo()
print md.add(1, 2).add(3,8,7,9).add((3,3,5)).subtract((4, 2), 5).result