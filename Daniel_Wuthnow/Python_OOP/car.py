class car(object):
	
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
				
	def display_all(self):
		if self.price > 10000:
			tax = .15
		else:
			tax = .12
		print "Price: {}".format(self.price)
		print "Speed: {}".format(self.speed)
		print "Fuel: {}".format(self.fuel)
		print "Mileage: {}".format(self.mileage)
		print "Tax: {}".format(tax)
		return self
car1 = car(2000,35,"Full", 50000) 
car1.display_all()
car2 = car(40000,135,"Empty", 5) 
car2.display_all()
car3 = car(1000,15,"full", 2000000) 
car3.display_all()
car4 = car(25000,75,"full", 50000) 
car4.display_all()
car5 = car(2000,35,"full", 50000) 
car5.display_all()
car6 = car(2000,35,"full", 50000) 
car6.display_all()