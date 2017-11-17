class Animal(object):
	def __init__(self,name,health):
		self.name=name
		self.health=health
	def walk(self):
		self.health -=1
		return self
	def run(self):
		self.health -=5
		return self
	def displayHealth(self):
		print "The {} Health: {}".format(self.name,self.health)
		return self

animal1 =Animal('Kitty',120)
animal1.walk().walk().walk()
animal1.run().run()
animal1.displayHealth()
print "--------------------------"

class Dog(Animal):
	def __init__(self,name):
		super(Dog,self).__init__(name,150)
		#self.health =150

	def pet(self):
		self.health +=5
		return self

dog1 = Dog("Bulldog")
dog1.walk().walk().walk()
dog1.run().run()
dog1.pet()
dog1.displayHealth()

print "------------------------------"


class Dargon(Animal):
	def __init__(self, name):
		super(Dargon,self).__init__(name,170)
		#self.health = 170

	def fly(self):
		self.health -=10
		return self

	def displayHealth(self):
		super(Dargon,self).displayHealth()
		print  "I am a Dragon"

dargon1 =Dargon("RedDargon")
dargon1.fly()
dargon1.displayHealth()