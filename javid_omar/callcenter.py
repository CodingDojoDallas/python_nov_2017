class Call(object):
	def __init__(self,id_,name,phnum,time,reason):
		self.id_=id_
		self.name=name
		self.phnum=phnum
		self.time=time
		self.reason=reason
	def display(self):
		print self.id_
		print self.name
		print self.phnum
		print self.time
		print self.reason
class CallCenter(object):
	def __init__(self):
		self.calls=[]
		self.queuesz=len(self.calls)
	def add(self,newcall):
		self.calls.append(newcall)
		self.queuesz=len(self.calls)
		return self
	def remove(self):
		self.calls.pop(0)
		self.queuesz=len(self.calls)
		return self
	def info(self):
		for element in self.calls:
			print element.name
			print element.phnum
		print self.queuesz
	def removenum(self,num):
		count=0
		for element in self.calls:
			if element.phnum==num:
				break
			count+=1
		self.calls.pop(count)
		self.queuesz=len(self.calls)
		print str(num)+" call. has been removed from the queue"
		return self




a=Call("69","bob",214000,300,"payment")
b=Call("78","vagene",972000,400,"payment")
c=Call("99","pls",977000,500,"payment")
x=CallCenter()
x.add(a).add(b).add(c).info()
x.removenum(972000)