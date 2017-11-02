class car(object):

    def __init__(self, price, speed, fuel, mileage):
        self.price =price
        self.speed =speed
        self.fuel =fuel
        self.mileage =mileage
        if price > 10000:
            self.tax =.15
        else:
            self.tax =.12
        self.display_all()

    def display_all(self):
        print 'price:' + str(self.price)
        print 'speed:' + str(self.speed) + 'mph'
        print 'fuel:' + str(self.fuel)
        print 'mileage:' + str(self.mileage) + "mpg"
        print 'tax:' + str(self.tax)




car1 = car(20000,"75mph","full","20mpg")
car2 = car(25000,"85mph","empty","30mpg")
car3 = car(5000, "30mph","half full","90mpg")
car4 = car(9000, "55mph","full","40mpg")
car5 = car(2000000, "315mph","empty","10mpg")
car6 = car(1000, "20mph", "empty","35mpg")
