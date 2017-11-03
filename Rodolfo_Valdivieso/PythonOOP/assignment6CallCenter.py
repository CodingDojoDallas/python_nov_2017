#Assignment 6 OOP - Call Center

class call(object):
	def __init__(self, uniqueID, callerName, callerPhone, callTime, callReason):
		self.uniqueID = uniqueID
		self.callerName = callerName
		self.callerPhone = callerPhone
		self.callTime = callTime
		self.callReason = callReason

	def display(self):
		print "ID           : " , self.uniqueID
		print "Caller Name  : " , self.callerName
		print "Caller Phone : " , self.callerPhone
		print "Caller Time  : " , self.callTime
		print "Caller Reason: " , self.callReason
		return self

class CallCenter(object):
	def __init__(self):
		self.calls = []
		self.queueSize = 0

	def add(self, call):
		self.calls.append(call)
		self.queueSize += 1

	def remove(self):
		if len(self.calls) > 0:
			self.calls.pop(0)
			self.queueSize -= 1

	def info(self):
		print "Lenght of the queue: " , self.queueSize
		for i in self.calls:
			print "Name: " + i.callerName + ", Phone: " + i.callerPhone

	def removeByPhone(self, phone):
		for i in range(0, len(self.calls)-1):
			if self.calls[i].callerPhone == phone:
				print "Removing: " , self.calls[i].callerName
				self.calls.pop(i)
				self.queueSize -= 1

	def sortList(self):
		self.calls.sort(key = lambda x: x.callTime)



call1 = call(1, "John", "469425789", "2:50pm", "Sale");
call2 = call(2, "Mike", "222222222", "3:50pm", "Customer Service");
call3 = call(3, "Last", "3333333", "4:50pm", "Invalid");
call4 = call(4, "First", "3333333", "1:50pm", "Invalid");
call5 = call(5, "Second", "3333333", "3:50pm", "Invalid");

call1.display()
call2.display()
call3.display()

print "Call Center:::::"
CallCenter1= CallCenter()
CallCenter1.add(call1)
CallCenter1.add(call2)
CallCenter1.add(call3)
CallCenter1.add(call4)
CallCenter1.add(call5)
CallCenter1.remove()
CallCenter1.removeByPhone("222222222")
print "Before Sorting::::::::"
CallCenter1.info()
CallCenter1.sortList()
print "After sorting:::::::::::"
CallCenter1.info()