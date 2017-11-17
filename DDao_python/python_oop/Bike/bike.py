class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print "Price of the bike is: $" + str(self.price)
        print "The max speed is:" + str(self.max_speed)
        print "Total miles:" + str(self.miles)

    def ride(self):
        print "Riding"
        self.miles += 10

    def reverse(self):
        if self.miles > 0:
            self.miles -=5
        print "Reversing"

bike1 = Bike(500, 20)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()

bike2 = Bike(129.99, 13)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()

bike3 = Bike(1000, 30)
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayinfo()