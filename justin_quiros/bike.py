class Bike(object):
	
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed =  max_speed
		self.miles = 0
	def displayinfo(self):
		print "Price is $: " + str(self.price) 
		print "Max speed is: " + str(self.max_speed) + " mph"
		print "Total miles: " + str(self.miles) + " miles"
		return self
	def ride(self):
		print "Riding"
		self.miles += 10
		return self
	def reverse(self):
		print "Reversing"
		self.miles -= 5
		if self.miles < 0:
			self.miles = 0
		return self


Bike1 = Bike(300, "15")
Bike2 = Bike(250, "10")
Bike3 = Bike(450, "20")



Bike1.ride().ride().ride().reverse().displayinfo()

Bike2.ride().ride().reverse().reverse().displayinfo()

Bike3.reverse().reverse().reverse().displayinfo()

