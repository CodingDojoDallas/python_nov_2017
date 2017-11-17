class Call(object):
	def __init__(self,uniqueId,callerName,callerPhonenum,timeofCall,reasonforCall):
		self.uniqueId=uniqueId
		self.callerName=callerName
		self.callerPhonenum=callerPhonenum
		self.timeofCall=timeofCall
		self.reasonforCall=reasonforCall

	def display(self):
		print "Id #:",self.uniqueId
		print "Caller Name:",self.callerName
		print "Caller Phone# :",self.callerPhonenum
		print "Time Of Call :",self.timeofCall
		print "Reason for Call :",self.reasonforCall
		return self

call1= Call(1,'rashid','3476058728','12:30am','Internet not working')
call1.display()

class CallCenter(object):
	def __init__(self):
		self.calllist=[]
		self.queuesize =0

	def add(self,call):
		self.calllist.append(call)
		self.queuesize +=1

	def remove(self):
		if len(self.calllist)>0:
			self.calllist.pop(0)
			self.queuesize -=1

	def info(self):
		for i in self.calllist:
			print "Caller Id :", str(i.uniqueId)
			print "Caller Name ", str(i.callerName)
			print "Caller Phone#", str(i.callerPhonenum)
		print "lenght of call ",self.queuesize

#Ninja Level def removePhone(self,num):




#Hacker Level def sortCallerList(self,)

call2 =Call(3,'Sawan','9807654345','11:00AM', 'NetWork is not Working')
call3 = Call(4, 'lee','4073481098',"12:00PM", 'Gps not Working')
call4 =Call(2,'William','2345679876','1:00AM','Sim Activation')
call5 = Call(5, 'mikal','3456789021','3:00PM', 'Information')

call2.display()

callcenter1 = CallCenter()
callcenter1.add(call2)
callcenter1.add(call3)
callcenter1.add(call4)
callcenter1.add(call5)
callcenter1.info()




