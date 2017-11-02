class MathDojo(object):
	def __init__(self, num =0):
		
		 self.num = num
		

	def add(self, a, b):
		self.num += (a + b)
		# print self.result
		return self

	def sub(self, s, t):
		self.num -= (s + t)
		# print self.result
		return self
	def res(self):
		print self.num
md = MathDojo()
md.add(0,2).add(2,5).sub(3,2).res()

Part Deux

class MathDojo(object):
	def __init__(self, num):
		
		 self.num = num
		

	def add(self, a, b, arr):
		self.num += (a + b)+[arr]
		# print self.result
		return self

	def sub(self, s, t, arr):
		self.num -= (s + t)-[arr]
		# print self.result
		return self
	def res(self):
		print self.num
md = MathDojo()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result

class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result += k
            else:
                self.result += i
        return self
    def res(self):
    	print self.result
    	return self

md = MathDojo()      
md.add([1], 3,4).add([3,5,7,8], [2,43,125]).res()





  
