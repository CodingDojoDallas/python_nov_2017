class Call(object):
	def __init__(self, id, name, number):
	self.unique_id = unique_id
	self.caller_name = caller_name
	self.caller_phone_num = caller_phone_num
	self.time_of_call = time_of_call
	self.reason_for_call = reason_for_call

	def display(self):
		print self.unique_id
		print self.caller_name
		print self.caller_phone_num
		print self.time_of_call
		print self.reason_for_call


class CallCenter(object):
	def __init__(self, tuple, size)
		self.calls = []
		self.queue_size = len(self.calls)

	def add(self):
		self.calls.append(new_call)

	def remove(self):
		self.call.remove(self.calls[0])

	def info(self):
		for call in self.calls:
			print self.caller_name
			print self.caller_phone_num
			print self.queue_size

