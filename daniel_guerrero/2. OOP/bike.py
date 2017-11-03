class Bike(object):
	def __init__(self, price, max_speed, miles=0):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles

	def displayInfo(self):
		print "The price is: $ {}" .format(self.price)
		print "The max speed is {}" .format(self.max_speed)
		print "This baby has {} miles!" .format(self.miles)

	def ride(self):
		print "Riding"
		self.miles += 10
		return self

	def reverse(self):
		print "Reversing"
		if self.miles > 5:
			self.miles -= 5
		return self

bike1 = Bike(99.99, 15, )

bike1.displayInfo()