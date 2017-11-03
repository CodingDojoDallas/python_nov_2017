#Assignment 5 Python OOP - Math Dojo

#PART 1

class MathDojo(object):
	def __init__(self):
		self.result = 0

	def add(self, *a):
		for i in a:
			self.result += i
		return self

	def substract(self, *a):
		for i in a:
			self.result -= i
		return self

md = MathDojo()
print md.add(2).add(2,5).substract(3,2).result

#PART 2
class MathDojo2(object):
	def __init__(self):
		self.result = 0

	def add(self, *a):
		for i in a:
			#if is a single integer then....
			if type(i) == int:
				self.result += i
			else:
			#else then, it is a list.......
				for x in i:
					self.result += x
		return self


	def substract(self, *a):
		for i in a:
			#if is a single integer then....
			if type(i) == int:
				self.result -= i
			else:
			#else then, it is a list.......
				for x in i:
					self.result -= x
		return self

md2 = MathDojo2()
print md2.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).substract(2, [2,3], [1.1,2.3]).result

#PART 3
#same as part 2, it works for both cases......

md3 = MathDojo2()
print md3.add([1], 3,4).add((3,5,7,8), [2,4.3,1.25]).substract(2, [2,3], (1.1,2.3)).result
