from datetime import datetime

class Call(object):
	uniqid = 0

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
	
	def __init_(self, calls):
		self.queue = 0
		self.calls = []
	def call_add(self, Call):
		self.call_add
	# def call_remove(self):
	# 	self.call_remove.remove(self.queue)


caller1 = Call("Justin", 5555555555, "need help")
caller2 = Call("John", 5555552222, "need help")
caller3 = Call("Sally", 5555553333, "need help")

Call_Hub = Call_Center()

Call_Hub.call_add(caller1)








