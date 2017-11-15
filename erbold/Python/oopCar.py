
# OOP Car:

# -Create a class called Car
# -In the __init__() allow the user to specify the following attributes: 
# price, speed, fuel, mileage
# -If the price is greater than 10,000 set the tax to be 15%, else set the tax to be 12%
# -Create 6 different instances of the class Car
# -In the class have a method called display_all() that returns all the information 
# about the car as a string. In your __init__(), call this display_all() method to 
# display information 


# Code:

class Car(object):
    
    def __init__(self, price, speed, fuel, mileage): 
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.display_all()


    def display_all(self):
        print "price: " + str(self.price)
        print "speed: " + str(self.speed) + " mph"
        print "fuel: " + self.fuel
        print "mileage: " + str(self.mileage) + " mpg"
        if self.price < 10000:
            print "tax: 12%"
        else:
            print "tax: 15%"

car1=Car(2000, 35, 'Full', 15)
car2=Car(200000, 35, 'Empty', 15)

