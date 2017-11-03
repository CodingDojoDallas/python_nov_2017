class animal(object):
	"""docstring for animal"""
	def __init__(self, name, health):
		self.name = name
		self.health = health
	def walk(self):
		self.health -= 1
	def run(self):
		self.health -= 5
	def display_health(self):
		print "Your {} HP is now {}".format(self.name, self.health)
		
# animal = animal('cat', 300)
# animal.walk().walk().walk().run().run().display_health()

class dog(animal):
	"""docstring for dog"""
	def __init__(self, name):
		super(dog, self).__init__(name, 150)
	def pet(self):
		self.health += 5
		return self
# dog1 = dog('polkadot')
# dog1.walk().walk().walk().run().run().pet().display_health()

class dragon(animal):
		"""docstring for dragon"""
		def __init__(self, name):
			super(dragon, self).__init__(name, 170)
		def fly(self):
			self.health -= 10;
			return self
		def display_health(self):
			#print "Your {} HP is now {}".format(self.name, self.health)
			super(dragon, self).display_health()
			print "Im a dragon"
# dragon1 = dragon('toothless')
# dragon1.fly().fly().display_health()

class cat(animal):
	"""docstring for cat"""
	def __init__(self, name):
		super(cat, self).__init__(name, 150)
	def purr(self):
		self.health += 30
		return self
	def squezzes(self):
		self.health -= 5
		return self
	def display_health(self):
		super(cat, self).display_health()
		print "I love my Tia <3"
Buggy = cat('Buggy')
Buggy.squezzes().squezzes().purr().display_health()

				