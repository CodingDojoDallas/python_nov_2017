'''Animal'''

class Animal(object):
    def __init__(self, name = "Animal", health = 100):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "{}'s health: {}".format(self.name, self.health)
        return self

# animal1 = Animal("Poopy Animal", 100)
# animal1.walk().walk().walk()
# animal1.run().run()
# animal1.displayHealth()
# #animal1.pet().fly()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

dog1 = Dog("Doggy")
dog1.walk().walk().walk().run().run().pet()
dog1.displayHealth()
#dog1.fly()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self
    
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon"
        return self

dragon1 = Dragon("Draggy")
dragon1.displayHealth()
dragon1.fly()
dragon1.displayHealth()
dragon1.walk()
dragon1.displayHealth()