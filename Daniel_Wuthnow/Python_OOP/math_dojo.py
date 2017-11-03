# class MathDojo(object):
# 	"""docstring for MathDojo"""
# 	def __init__(self, num=0):
# 		self.num = num
# 	def add(self, a, b):
# 		self.num = self.num +(a+b)
# 		return self
# 	def sub(self, s, t):
# 		self.num = self.num - (s+t)
# 		return self
# 	def result(self):
# 		print self.num		
# md = MathDojo()
# md.add(0,2).add(2,5).sub(3,2).result()


# class MathDojo(object):
# 	"""docstring for MathDojo"""
# 	def __init__(self, num, arr, *gggg):
# 		self.num = num
# 		self.arr = arr
# 	def add(self, a, b):
# 		self.num = self.num +(a+b)
# 		return self
# 	def sub(self, s, t):
# 		self.num = self.num - (s+t)
# 		return self
# 	def result(self):
# 		print self.num		
# md = MathDojo(2,[1,2,3])

#part 2
class MathDojo(object):
	"""docstring for MathDojo"""
	def __init__(self):
		self.result = 0
	def add(self, *a):
		for i in a:
			if type(i) == int:
				self.result += i
			else:
				for x in i:
					self.result += x
		return self

	def sub(self, *a):
		for i in a:
			if type(i) == int:
				self.result -= i
			else:
				for x in i:
					self.result -= x
		return self
	def total(self):
		print self.result


md = MathDojo()
md.add([1], 3,4).add([3,5,7,8], [2,4,3,1]).sub((2,3), [2,3], [1.1,2,3]).total()

#part 3 same as part 2