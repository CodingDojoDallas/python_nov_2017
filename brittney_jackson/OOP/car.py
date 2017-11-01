class Car(object):

	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
#		if price > 10000:
#			self.tax = 0.15
#		else:
#			self.tax - 0.12
		self.displayAll()

	def displayAll(self):
		print "Price:"+str(self.price)
		print "Speed:"+str(self.speed)
		print "Fuel:"+str(self.fuel)
		print "Mileage:"+str(self.mileage)
#		print "Tax:"+str(self.tax)


newCar1 = Car(9000,'20mph','Tank on E','30mpg')

newCar2 = Car(2200,'60mph','Quarter full','20mpg')

newCar3 = Car(23000,'45mph','Driving on Jesus','15mpg')

newCar4 = Car(17000,'0mph','Tank on F','35mpg')

newCar5 = Car(120000,'27mph','Half full','25mpg')

newCar6 = Car(500000,'50mph','no fuel: Electric car','NA')