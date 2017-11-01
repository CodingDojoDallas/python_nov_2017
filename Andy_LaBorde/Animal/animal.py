class animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health
	

	def walk(self):
		self.health = self.health -1 
		return self
	def run(self):
		self.health = self.health -5
		return self
	def disHealth(self):
		print "Your {}'s HP is now {}".format(self.name, self.health)

animal1 = animal('dog', 100)

animal1.walk().walk().walk().run().run().disHealth()

class Dog(animal):
	def __init__(self, name):
		super(Dog, self).__init__(name, 150)
	def pet(self):
		self.health += 5
		return self
dog1 = Dog('Clifford')

dog1.walk().run().pet().disHealth()

class Dragon(animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name, 170)
	def fly(self):
		self.health -= 10
		return self
	def disHealth(self):
		# super(Dragon, self).disHealth()
		print "Your {}'s HP is now {}".format(self.name, self.health)
		print "I'm a Dragon Biiiish!!"
dragon1 = Dragon('Charizard')
dragon1.fly().disHealth()

class Pig(animal):
	def __init__(self, name):
		super(Pig, self).__init__(name, 1000)
	def squeal(self):
		self.health += 50
		return self

pig1 = Pig('Porky')
pig1.run().run().walk().run().run().walk().run().run().walk().squeal().disHealth()











