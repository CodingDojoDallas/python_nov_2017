class bike(object):

    def __init__(self, price, maxSpeed):
        self.price = price
        self.maxSpeed = maxSpeed
        self.miles = 0

    def displayInfo(self):
        print "This bike costs  ${}. The max speed is {}mph and currently has {} miles on it.".format(self.price, self.maxSpeed, self.miles)
        #return self

    def ride(self):
        print "riding!"
        self.miles =self.miles +10
        return self

    def reverse(self):
        print "reversing!"
        self.miles -= 5
        if self.miles <0:
            self.miles = 0
        return self

bike1=bike(4000, '45mph')


bike1.ride().ride().ride().reverse()
bike1.displayInfo()
