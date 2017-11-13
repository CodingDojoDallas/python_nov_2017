# OOP Animal

class Animal(object):

	def __init__(self, name, health):
		self.name = name
		self.health = health

	def walk(self):
		self.health = self.health - 1

	def run(self):
		self.health = self.health - 5

	def display_health(self):
		print (self.health)

Animal1 = Animal('Yap', 100)
Animal1.walk()
Animal1.walk()
Animal1.walk()
Animal1.run()
Animal1.run()
Animal1.display_health()


class Dog(Animal):

	def __init__(self, name, health):
		super(Dog, self).__init__(name, health)
		self.health = 150
	def pet(self):
		self.pet = self.health + 5

dog = Dog('Love', 100)
dog.walk()
dog.walk()
dog.walk()
dog.run()
dog.run()
dog.pet()
dog.display_health()

class Dragon(Animal):

	def __init__(self, name, health):
		super(Dragon, self).__init__(name, health)
		self.health = 170
	def fly(self):
		self.health = self.health - 10
	def display_health(self):
		print ("I am a Dragon")
		super(Dragon, self).display_health()

dragon = Dragon("Kracker", 100)
dragon.fly()
dragon.display_health()
