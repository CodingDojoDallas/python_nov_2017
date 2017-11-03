#Assigment 2 Python OOP - Car
#Car Class

class car(object):
	# the __init__ method is called every time a new object is created
    def __init__(self, price, speed, fuel, mileage):
        # set some instance variables. just like any variable we can call these anything
        self.price = price
        self.speed = speed
        self.fuel  = fuel
        self.mileage = mileage
        if price > 10000:
        	self.tax  = 15
        else:
        	self.tax  = 12
        print self.display_all()


    def display_all(self):
    	string = "Price: " + str(self.price) +"\nSpeed: " + self.speed +"\nFuel: " + self.fuel +"\nMileage: " + self.mileage +"\nTax: " +str(self.tax)
    	return string
 

car1 = car(2000, "35mph", "Full", "15mpg")
car2 = car(2000, "5mph", " Not Full", "105mpg")
car3 = car(2000, "15mph", "Kind of Full", "95mpg")
car4 = car(2000, "25mph", "Full", "25mpg")
car5 = car(2000, "45mph", "Empty", "25mpg")
car6 = car(20000000, "35mph", "Empty", "15mpg")
