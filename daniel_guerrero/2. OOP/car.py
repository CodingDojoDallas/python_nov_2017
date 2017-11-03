class Car(object):
	def __init__(self, price, speed, fuel, mileage, tax=.12):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = tax

		if self.price > 10000:
			self.tax = .15

	def displayAll(self):
		print """The price of this vehicle is {}, its speed is {}, its fuel level is {}, its mileage is {}, 
		its sales tax is {}""".format(self.price, self.speed, self.fuel, self.mileage, self.tax)

car1 = Car(11000, 60, "full",60000).displayAll()
