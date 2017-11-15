# -Create a new class called Bike w/ the following properties/attributes:
# 	-price
# 	-max_speed
# 	-miles
# -Create 3 instances of the Bike class:
# -Use the _init_() function to specify the price and max_speed of each instance (e.g. bike1= Bike(200, "25mph"));
# 	-In the _init_() also write code so that the initial miles is set to 0 whenever a new instance is created
# -Add the following functions to this class:
# 	-displayinfo(): have this method display the bike's price, maximum speed, and the total miles
# 	-ride(): have it display "Riding" on the screen and increase the total miles ridden by 10
# 	-reverse(): have it display "Reversing" on the screen and decrease the total miles ridden by 5
# -Have the first instance ride three times, reverse once and have it displayInfo(). Have the 2nd instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().
# -What would you do to prevent the instance from having negative miles?
# -Which methods can "return self" in order to allow chaining methods? 

# ***

# class Employee:
	
# 	def _init_(self, first, last, pay):
# 		self.first=first
# 		self.last=last
# 		self.pay=pay
# 		self.email=first+'.'+last+'@company.com'

# 	def fullname(self):
# 		return '{}{}'.format(self.first,self.last)

# emp_1=Employee('Corey', 'Schafer', 50000) 
# emp_2=Employee('Test', 'User', 60000)

# emp_1.fullname()
# print(Employee.fullname(emp_1))

# ***

class Bike(object):
	def _init_(self, price, max_speed):
		self.price=price
		self.max_speed=max_speed
		self.miles=0

	def displayInfo(self):
		print 'Price is: $' + str(self.price)
		print 'Max speed:' + str(self.max_speed) + 'mph'
		print 'Total miles:' + str(self.miles) + 'miles'

	def drive(self):
		print 'Driving'
		self.miles += 10

	def reverse(self):
		print 'Reversing'
		#prevent negative miles
		if self.miles >= 5:
			self.miles -= 5


 #creating instances and run methods

bike1 = Bike(99.99, 12)
bike1.drive()
bike1.drive()
bike1.drive()
bike1.reverse()
bike1.displayinfo()

bike2 = Bike(102.99, 12)
bike2.drive()
bike2.drive()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()

bike3 = Bike(56.23, 100)
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayinfo()


	