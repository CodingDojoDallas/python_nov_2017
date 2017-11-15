from datetime import datetime

global counter 
counter = 0

class Call(object):
    def __init__(self, name, phone, time, reason):
        self.caller_name = name
        self.caller_phone = phone
        self.time = parse(time)
        self.reason = reason
        global counter
        counter+=1
        self.unique_id = counter

    def Display(self):
        print "Caller Id: " + str(self.unique_id)
        print "Caller Name: " + str(self.caller_name)
        print "Caller Phone #: " + str(self.caller_phone)
        print "Time of Call: " + str(self.time)
        print "Reason: " + str(self.reason)
        print ""

        return self
#testing
c1 = Call("Tom", "469-583-5414", "4:36", "just because")
c1.Display()
c2 = Call("Bill", "469-513-5314", "2:36", "reorder")
c3 = Call("Jeff", "510-813-9614", "12:15", "missing limb")
c4 = Call("Jane", "521-843-0611", "1:19", "order")
c5 = Call("Sarah", "210-366-4715", "5:10", "order status")


class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    def add(self, call):
        self.calls.append(call)
        self.queue_size+=1
        return self

    def remove(self, call):
        self.calls.remove(call)
        self.queue_size-=1
        return self

    def info(self):
        print "There are {} calls in queue.".format(self.queue_size)
        for idx in self.calls:
            print idx.caller_name + " " + str(idx.caller_phone)
        print ""
        return self

    #def sort(self):
    #    self.calls.sort(self.calls, key=)
    #    return self



call_center = CallCenter()
call_center.add(c1).add(c2).add(c3).add(c4).add(c5).info()

call_center.remove(c2).info()

#call_center.sort().info()

