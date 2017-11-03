class MathDojo(object):
	def __init__(self,val=0):
		self.num=val
	def add(self,*args):
		for arg in args:
			if type(arg)==list:
				for i in range(len(arg)):
					self.num+=arg[i]
			elif type(arg)==tuple:
				for i in range(len(arg)):
					self.num+=arg[i]
			else:
				self.num+=arg
		return self
	def sub(self,*args):
		for arg in args:
			self.num-=int(arg)
		return self

md=MathDojo()
md.add(2).add(2,5,[3,3,3],(1,1)).sub(3,2)
print md.num