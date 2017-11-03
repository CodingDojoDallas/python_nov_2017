class product(object):
	
	def __init__(self, price, name, weight, brand, status="for sale"):
		self.price = price
		self.name = name
		self.weight = weight
		self.brand = brand
		self.status = status
	
	def sell(self):
		self.status = "sold"
		return self

	def add_tax(self, t):
		self.price = self.price + (self.price * t)
		return self

	def returns(self, status, open):
		if status == 'defective':
			self.price = 0
			self.status = 'defective'
		if open == 'true':
			status = 'used'
			self.price = self.price * .80
		return self

	def display(self):
		print "Price is ${}".format(self.price)
		print self.name
		print self.weight
		print self.brand
		print self.status


product1 = product(10, 'shoes', 20, "ironshore")
product1.add_tax(.12).sell().display()
# product1.returns('for sale','true').display()