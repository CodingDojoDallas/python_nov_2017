class Car(object):
    def __init__(self, price,speed,fuel,mileage):
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        if price >10000:
            self.tax = 0.15
        else:
            self.tax= 0.12
        self.display_all()

   
    def display_all(self):
        print 'Price' ,self.price
        print 'Speed',self.speed
        print 'Fuel',self.fuel
        print 'Milage',self.mileage
        print 'Tax' ,self.tax

car1 = Car(2000, 35,'FULL',15)      
car2 = Car(2000, 5, 'Not Full',105)      
car3 = Car(2000, 15,'Kind of Full',95)      
car4 = Car(2000, 25,'Full', 25)  
car5 = Car(2000,45,"Empty",25)     
car5 = Car(20000000, 35,'Empty',15)     
