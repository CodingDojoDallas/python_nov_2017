global counter
counter = 1000

class Call(object):

	def __init__(self, name, phone, time, reason):
		self.name = name
		self.phone = phone
		self.time = time
		self.reason = reason
		global counter
		counter +=1
		self.gid = counter


	
		#print self.queue

	def display(self):
		print 'Caller Name: ' +self.name 
		print 'Caller Number: ' +self.phone 
		print 'Call Time: ' +self.time 
		print 'Call Reason: ' +self.reason 
		print 'Unique ID: ' +str(self.gid)
		#print 'Queue Position:' +self.queue 

class CallCenter(object):

	def __init__(self):
		self.calls = []
		self.queueSize = 0

	def add(self,caller):
		self.calls.append(caller)
		self.queueSize +=1 
		return self

	def endCall(self, caller):
		self.calls.remove(caller)
		self.queueSize -=1
		return self

	def info(self):
		print 'There are {} calls in the queue:'.format(self.queueSize)
		for i in self.calls:
			i.display()
			print ''
		return self	


newCall1 = Call('Jen', '555-1000', '2:30pm', 'lost debit card')
newCall2 = Call('Jena', '555-1001', '2:32pm', 'lost debit card')
#newCall1 = Call('Jen', '555-1000', '2:30pm', 'lost debit card')
#newCall1 = Call('Jen', '555-1000', '2:30pm', 'lost debit card')


cc1 = CallCenter()
cc1.add(newCall1).add(newCall2).info()
print '* * * * * * * *'
cc1.endCall(newCall1).info()




