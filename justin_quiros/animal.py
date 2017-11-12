class Animal(object):
	
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
		print self.health

# # Animal1 = Animal("Elephant", 100)

# Animal1.walk().walk().walk().run().run().display_health()


class Dog(Animal):

	def __init__(self, name):
		super(Dog, self).__init__(name, 150)

	def pet(self):
		self.health += 5
		return self

dog1 = Dog("Stella")
dog1.walk().walk().walk().run().run().pet().display_health()


class Dragon(Animal):

	def __init__(self, name):
		super(Dragon, self).__init__(name, 170)

	def fly(self):
		self.health -= 10
		# print self.health, "I am a Dragon"
		return self

dragon1 = Dragon("Drogon")
dragon1.fly().display_health()

class Kangaroo(Animal):

	def __init__(self, name):
		super(Kangaroo, self).__init__(name, 150)

	def hop(self):
		self.health -= 4
		return self

Kangaroo1 = Kangaroo("Kango")
Kangaroo1.hop().display_health()

# dog1.fly().display_health()