class Call(object):
	def __init__(self, num, name, time, reason):
		self.num = num
		self.name = name
		self.time = time
		self.reason = reason

	def display(self):
		print self.num
		print self.name
		print self.time
		print self.reason

class CallCenter(Call):
	def __init__(self, calls):
		super(CallCenter, self).__init__(num, name, time, reason)
		self.calls = []
		self.queueSize = 0
		

	def add(self, calls):
		
		self.queueSize += 1
		return self


	# def remove(self):


	def info(self):
		super(CallCenter, self).display()
		# print self.call
		print self.queueSize
		print self.calls

call1 = Call(123124123, 'john', '2:15', 'f.u.-thats why')
callCenter1 = CallCenter(10)

callCenter1.info()



