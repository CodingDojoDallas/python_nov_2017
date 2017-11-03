class Car(object):
	
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed =  speed
		self.fuel = ""
		self.mileage = mileage


			
	def display_all(self):
		if self.price > 10000:
			tax = .15
		else:
			tax = .12
		print "Price is $: " + str(self.price) 
		print "Speed is: " + str(self.speed) + " mph"
		print "Fuel: " + str(self.fuel)
		print "Mileage: " + str(self.mileage) + "mpg"
		print "Tax:" + str(tax)
		return self


Car1= Car(8000, 20, "Full", 30)
Car2= Car(10000, 25, "Empty", 15)
Car3= Car(22000, 45, "Kind of Full", 20)
Car4= Car(6000, 22, "Empty", 25)
Car5= Car(5300, 10, "Full", 15)
Car6= Car(6900, 40, "Full", 35)

Car1.display_all()
Car2.display_all()
Car3.display_all()
Car4.display_all()
Car5.display_all()
Car6.display_all()




