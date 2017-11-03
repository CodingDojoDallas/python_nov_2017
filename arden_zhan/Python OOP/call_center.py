'''Call Center'''

class Call(object):
    def __init__(self, uniqueID, name, phone, time, reason):
        self.uniqueID = uniqueID
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason

    def display(self):
        print "Unique ID: {}".format(self.uniqueID)
        print "Caller Name: {}".format(self.name)
        print "Caller Phone Number: {}".format(self.phone)
        print "Time of Call: {}".format(self.time)
        print "Reason for Call: {}".format(self.reason)
        return self

class CallCenter(object):
    def __init__(self, calls):
        self.calls = calls #list of call objects
        self.queue = len(self.calls)
    
    def add(self, call):
        self.calls.append(call)
        self.queue = len(self.calls)
        return self
    
    def remove(self):
        self.calls.pop(0) #remove first call from list
        self.queue = len(self.calls)
        return self
    
    def info(self):
        print "Queue Length: {}".format(self.queue)
        for x in range(self.queue):
            print "{}. {}: {}".format(x + 1, self.calls[x].name, self.calls[x].phone)

    '''Ninja Level'''
    def removeCall(self, phone):
        for x in self.calls:
            if x.phone == phone:
                self.calls.pop(self.calls.index(x)) 
        self.queue = len(self.calls)
        return self

    '''Hacker Level'''
    # key functions https://wiki.python.org/moin/HowTo/Sorting
    # key parameter used to specify function to be called on each list item prior to comparisons
    def sortTime(self):
        self.calls = sorted(self.calls, key = lambda call: call.time) # sort by time
        return self

call1 = Call(1111, "name1", "111-1111", 1, "reason1")
call2 = Call(2222, "name2", "222-2222", 2, "reason2")
call3 = Call(3333, "name3", "333-3333", 3, "reason3")
# call1.display()
# call2.display()

callcenter1 = CallCenter([call1, call2, call3])
callcenter1.add(call1).remove().info()
callcenter1.sortTime().info()
callcenter1.removeCall("222-2222").info()

