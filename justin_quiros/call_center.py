from datetime import datetime

class Call(object):
	uniqid = 1
	def __init__(self, callname, callnum, callreas):
		self.idnum = Call.uniqid
		self.callname = callname
		self.callnum = callnum
		self.calltime = datetime.now()
		self.callreas = callreas

		Call.uniqid += 1

	def call_display(self):
		print self.idnum
		print self.callname
		print self.callnum
		print self.calltime
		print self.callreas
		return self


class Call_Center(object):
	calls = []

	def __init_(self):
		self.calls = []
		self.queue = self.queue_size()

	def queue_size(self):
		print len(self.calls)

	def add(self, add_call):
		self.calls.append(add_call)
		return self
	def remove(self, del_call):
		self.calls.remove(del_call)
		return self

	def info(self):
		for x in self.calls:
			x.call_display()

caller1 = Call("Justin", 5555555555, "need help")
caller2 = Call("John", 5555552222, "need help")
caller3 = Call("Sally", 5555553333, "need help")

call_hub = Call_Center()

call_hub.add(caller1)
call_hub.add(caller2)
call_hub.add(caller3)
call_hub.queue_size()







