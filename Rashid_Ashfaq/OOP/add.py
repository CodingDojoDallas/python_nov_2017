class Vehicle(object):
	def __init__(self,wheels,capacity,make,model):
		self.wheels=wheels
		self.capacity=capacity
		self.make=make
		self.model=model
		self.mileage=0
	def drive(self,miles):
		self.mileage+=miles
		return self
	def reserve(self,miles):
		self.mileage -=miles
		return self
class Bike(Vehicle):
	def vehicle_type(self):
		return "Bike"
class Car(Vehicle):
	def set_wheel(self):
		self.wheels=4
		return self
class Airplane(Vehicle):
	def fly(self,miles):
		self.mileage+=miles
		return self
v = Vehicle(8,1,'Rashidmake','Tahirmodle')
print v.make
b =Bike(2,1,'hussainmake','putarimodel')
print b.vehicle_type()
c= Car(4,3,'maker1','modelt1')
c.set_wheel()
print c.wheels
a= Airplane(23,853,'PIA','NY')
a.fly(20)
print a.mileage