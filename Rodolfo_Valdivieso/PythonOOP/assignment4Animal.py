#Assignment 4 Python OOP - Animal

class animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def display_health(self):
		print "Health: " , self.health
		return self

print "Animal--------"
animal1 = animal("Spooky", 100)
animal1.walk().walk().walk().run().run().display_health()

class dog(animal):
	def __init__(self, name):
		super(dog, self).__init__(name, 150)

	def pet(self):
		self.health += 5
		return self
print "Dog--------"
dog1 = dog("Dog")
dog1.walk().walk().walk().run().run().pet().display_health()

class dragon(animal):
	def __init__(self, name):
		super(dragon, self).__init__(name, 170)

	def fly(self):
		self.health -= 10
		return self
	def display_health(self):
		super(dragon, self).display_health()
		print "I'm a Dragon"

print "Dragon--------"
dragon1 = dragon("Dragonnnn")
dragon1.fly().display_health()

print "Animal 2--------"
animal2 = animal("animal2", 200)
animal2.display_health()
#animal2.pet()
#animal2.fly()