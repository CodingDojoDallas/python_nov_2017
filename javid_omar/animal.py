class Animal(object):
	def __init__(self, name, health=10):
		self.name=name
		self.health=health
	def walk(self):
		self.health-=1
		return self
	def run(self):
		self.health-=1
		return self
	def display_health(self):
		print self.health

class Dog(Animal):
	def __init__(self,name):
		super(Dog, self).__init__(name,150)
	def pet(self):
		self.health+=5
		return self
class Dragon(Animal):
	def __init__(self,name):
		super(Dragon, self).__init__(name,170)
	def fly(self):
		self.health-=10
		return self
	def display_health(self):
		Animal.display_health(self)
		print "I am a Dragon"

cat=Animal("cat",15)
cat.walk().walk().walk().run().run().display_health()

bro=Dog("cool")
bro.walk().walk().walk().run().run().pet().display_health()

drogo=Dragon("lol")
drogo.walk().display_health()




