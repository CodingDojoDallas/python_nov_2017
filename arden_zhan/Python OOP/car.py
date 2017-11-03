'''Car'''

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if (price > 10000): self.tax = 0.15
        else: self.tax = 0.12
        self.display_all()

    def display_all(self):
        print "Price: {}".format(self.price)
        print "Speed: {}".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {}".format(self.mileage)
        print "Tax: {}".format(self.tax)

        return self

print "\nCar 1:"
car1 = Car(2000, "35mph", "Full", "15mph")

print "\nCar 2:"
car2 = Car(2000, "5mph", "Not Full", "105mph")

print "\nCar 3:"
car3 = Car(2000, "15mph", "Kind of Full", "95mph")

print "\nCar 4:"
car4 = Car(2000, "35mph", "Full", "15mph")

print "\nCar 5:"
car5 = Car(2000, "45mph", "Empy", "25mph")

print "\nCar 6:"
car6 = Car(2000000, "35mph", "Empty", "15mph")