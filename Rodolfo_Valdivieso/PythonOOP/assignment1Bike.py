#Assignment 1 Python OOP - Bike
#new class called Bike with the following properties/attributes
class bike(object):
	# the __init__ method is called every time a new object is created
    def __init__(self, price, max_speed):
        # set some instance variables. just like any variable we can call these anything
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
    	print "$" , self.price
    	print self.max_speed
    	print self.miles , " miles"
    	return self
    def ride(self):
    	self.miles = self.miles + 10
    	print "Riding........"
    	return self

    def reverse(self):
    	print "Reversing......."
    	if (self.miles >= 5):
    		self.miles = self.miles - 5
    	return self


bike1 = bike(1500, "15mph")
bike2 = bike(1500, "15mph")
bike3 = bike(1500, "15mph")

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()