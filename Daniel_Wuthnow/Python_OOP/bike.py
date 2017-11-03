class bike(object):
	"""docstring for ClassName"""
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayinfo(self):
		print "${}".format(self.price)
		print "{}mph".format(self.max_speed)
		print "Gone {} miles".format(self.miles)
		return self
	def ride(self):
		print "Riding"
		self.miles += 10
		return self
	def reverse(self):
		print "Reverseing"
		self.miles -= 5
		if self.miles < 0:
			self.miles = 0
		return self

bike1 = bike(400, 20)
bike2 = bike(250, 17)
bike3 = bike(250, 17)

# bike1.ride().ride().ride().reverse().displayinfo()
# bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()