class call(object):
	"""docstring for call_class"""
	def __init__(self, idu, name, number, time, reason):
		self.idu = idu
		self.name = name
		self.number = number
		self.time = time
		self.reason = reason
	def display(self):
		print self.idu
		print self.name
		print self.number
		print self.time
		print self.reason
# cl = call(12,'daniel', 5555555, 52, 'missed you')
# cl.display()




# what i need to finish it is to somehow how the info in an array so that i can read from in, but what i think i need to know is how to append the info into the array
class callcenter(call):
	"""docstring for callcenter"""
	def __init__(self, call):
		super(callcenter, self).__init__(123,'name',5555555,54,'missed you')
		self.calls = []
		self.que = 0
	def add(self):
		# super(callcenter,self).display()
		self.calls.append(super(callcenter,self).display()) 
		self.que += 1
		return self
	def remove(self):
		self.que -= 1
		return self

	def info(self):
		super(callcenter, self).display()
		print self.que
		print self.calls

caller = callcenter(1)
caller.add().info()
		