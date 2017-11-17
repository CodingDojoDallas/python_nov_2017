class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health
		self.display_health()

	def walk(self):
		self.health -= 1
		return self
		
	def run(self):
		self.health -= 5
		return self

	def display_health(self):
		print "Name: " + str(self.name)
		print "Health: " + str(self.health)

animal1 = Animal("Thor", 100)
animal1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
	def __init__(self, name, health):
		super(Dog, self).__init__(name, health)
		self.health = 150

	def pet(self):
		self.health += 5
		return self

dog1 = Dog("Shaggy", 150)
dog1.walk().walk().walk().run().run().pet().display_health()


class Dragon(Animal):
	def __init__(self, name, health):
		super(Dragon, self).__init__(name, health)
		self.health = 170

	def fly(self):
		self.health -= 10
		return self

	def display_health(self):
		print "This is a Dragon!"+ str(self.health)

dragon1 = Dragon("Oden", 170)
dragon1.walk().walk().walk().run().run().display_health()
