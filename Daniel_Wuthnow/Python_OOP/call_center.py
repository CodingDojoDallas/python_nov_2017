# class call(object):
# 	"""docstring for call_class"""
# 	def __init__(self, idu, name, number, time, reason):
# 		self.idu = idu
# 		self.name = name
# 		self.number = number
# 		self.time = time
# 		self.reason = reason
# 	def display(self):
# 		print self.idu
# 		print self.name
# 		print self.number
# 		print self.time
# 		print self.reason
# # cl = call(12,'daniel', 5555555, 52, 'missed you')
# # cl.display()




# # what i need to finish it is to somehow how the info in an array so that i can read from in, but what i think i need to know is how to append the info into the array
# class callcenter(call):
# 	"""docstring for callcenter"""
# 	def __init__(self, call):
# 		super(callcenter, self).__init__(123,'name',5555555,54,'missed you')
# 		self.calls = []
# 		self.que = 0
# 	def add(self):
# 		# super(callcenter,self).display()
# 		self.calls.append(super(callcenter,self).display()) 
# 		self.que += 1
# 		return self
# 	def remove(self):
# 		self.que -= 1
# 		return self

# 	def info(self):
# 		super(callcenter, self).display()
# 		print self.que
# 		print self.calls

# caller = callcenter(1)
# caller.add().info()
# 		



# from solutions
from datetime import datetime

class Call(object):
    NUM_CALLS = 0
    def __init__(self, caller, phone_num, reason):
        self.caller = caller
        self.phone_num = phone_num
        self.time_of_call = datetime.now()
        self.reason = reason
        self.id = Call.NUM_CALLS
        
        Call.NUM_CALLS += 1
    
    def display_info(self):
        print "\n" + ("#" * 20)
        for attr, val in self.__dict__.iteritems():
            if attr == "time_of_call":
                print "{}: {}".format(attr, val.strftime("%I:%M:%S"))
            else:
                print "{}: {}".format(attr, val)
        print "#" * 20

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = self.get_queue_size()

    def get_queue_size(self):
        return len(self.calls)

    def add(self, a_call):
        self.calls.append(new_call)

    def remove(self, r_call):
        self.calls.remove(r_call)

    def info(self):
        for call in self.calls:
            call.display_info()


'''
You can run this file to interactively add calls
'''


def handle_call():
    print "Would You like to make a call?"
    print "type [1] for yes and [0] for no"
    ans = raw_input()
    return int(ans)

def take_call():
    print "What is your name?"
    name = raw_input()
    print "What is your reason for calling?"
    reason = raw_input()
    print "Please confirm your phone number"
    num = raw_input()
    print "Please stay on the line while we proccess your call"
    return Call(name, num, reason)

game_on = True
center = CallCenter()
while game_on:
    ring = handle_call()
    if ring == 1:
        center.calls.append(take_call())
        print "All calls today:"
        center.info()
    else:
        game_on = False