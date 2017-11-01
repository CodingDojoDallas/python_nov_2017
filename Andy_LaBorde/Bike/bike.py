class bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print self.price, self.max_speed, self.miles
	def ride(self):
		print "Riding" 
		self.miles +=10
	def reverse(self):
		print "Reversing"
		if self.miles > 5:
			self.miles -=5
			# self.miles = 0

bike1 = bike(200,50)
bike1.displayInfo()
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.reverse()
bike1.displayInfo()

bike2 = bike(200, 50)
bike2.displayInfo()
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3 = bike(200, 50)
bike3.displayInfo()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()




