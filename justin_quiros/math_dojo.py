class MathDojo(object):
	def __init__(self):
		self.result = 0

	def add(self, *j):
		for i in j:
			if type(i) == int:
				self.result += i
			else:
				for x in i:
					self.result += x
		return self

	def subtract(self, *j):
		for i in j:
			if type(i) == int:
				self.result -= i
			else:
				for x in i:
					self.result -= x
		return self	

	def total(self):
		print self.result	

md = MathDojo()
# md.add([2,1,2],3).add(4,3).total()
md.subtract(2,3).subtract([1,2,4,3],2,3,2).total()
