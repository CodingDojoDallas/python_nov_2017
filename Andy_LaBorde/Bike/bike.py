
class bike(object):
	def __init__(self, name, price, max_speed):
		self.name = name
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print self.name, self.price, self.max_speed, self.miles
		return self
	def ride(self):
		print "Riding" 
		self.miles +=10
		return self
	def reverse(self):
		print "Reversing"
		if self.miles > 5:
			self.miles -=5
		return self
			# self.miles = 0

bike1 = bike('bike1', 200,50)
bike1.displayInfo().ride().ride().ride().reverse().reverse().displayInfo()

bike2 = bike('bike2', 200, 50)
bike2.displayInfo().ride().ride().reverse().reverse().displayInfo()

bike3 = bike('bike3', 200, 50)
bike3.reverse().reverse().displayInfo()




