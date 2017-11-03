class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price>10000:
			self.tax = .15
		else:
			self.tax = .12
		self.display_all()
	def display_all(self):
		print "Price: "+str(self.price)
		print "Speed: "+str(self.speed)
		print "Fuel: "+str(self.fuel)
		print "Mileage: "+str(self.mileage)
		print "Tax: "+str(self.tax)
		return self
car1 = Car(1000,"40mph","full","20mpg")

car2 = Car(11000,"50mph","full","40mpg")

car3 = Car(115000,"250mph","full","10mpg")

car4 = Car(9000,"60mph","half full","30mpg")

car5 = Car(1111000,"500mph","full","5mpg")

car6 = Car(100,"30mph","full","1mpg")
