class car(object):
	def __init__(self, price, speed, fuel, mileage):
		if price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.displayAll()

	def displayAll(self):
		print self.price
		print self.speed
		print self.fuel
		print self.mileage
		print self.tax

car1 = car(2000, 150, 'Full', 30000)

car2 = car(4000, 150, 'Almost Full', 2000)

car3 = car(750, 90, 'Almost Empty', 30000)

car4 = car(80000, 250, 'Full', 20)

car5 = car(3000, 100, 'Full', 1000)

car6 = car(2000, 150, 'Full', 80000)
