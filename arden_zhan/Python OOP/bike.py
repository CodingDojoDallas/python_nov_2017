'''Bike'''

class Bike(object):
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print "Bike Price: {}".format(self.price)
        print "Max Speed: {}".format(self.max_speed)
        print "Total Miles: {}".format(self.miles)
    
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self

print "\nBike 1:"
bike1 = Bike(200, "25mph")
bike1.ride().ride().ride()
bike1.reverse()
bike1.displayInfo()

print "\nBike 2:"
bike2 = Bike(100, "10mph")
bike2.reverse().reverse()
bike2.displayInfo()

print "\nBike 3:"
bike3 = Bike(50, "5mph")
bike3.reverse().reverse().reverse()
bike3.displayInfo()

'''To prevent instance from having negative miles, could just have check for miles saying if it's negative, reset it to 0
return self on the ride, reverse functions in order to chain them. displayInfo can have a return self too if you're not calling it last
'''