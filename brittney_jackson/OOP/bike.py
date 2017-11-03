#Create a class called Bike

class Bike(object):

	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayInfo(self):
		print "My bike costs ${}. It's max speed is {}. It currently has {} total miles.".format(self.price, self.max_speed, self.miles)
#        return self

	def ride(self):
		print "Riding!"
		self.miles = self.miles + 10
		return self

	def reverse(self):
		print "Reversing!"
		self.miles -= 5
		if self.miles <0:
			self.miles =0
		return self

		

newBike1 = Bike(200,'20mph')

newBike1.ride().ride().ride().reverse()
newBike1.displayInfo()

newBike2 = Bike(400,'30mph')

newBike2.ride().ride().reverse().reverse()
newBike2.displayInfo()

newBike3 = Bike(50,'5mph')

newBike3.reverse().reverse().reverse()
newBike3.displayInfo()



