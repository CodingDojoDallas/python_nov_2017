
class product(object):
	def __init__(self, price, item_name, weight, brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = 'for sale'

	def sell(self):
		self.status = 'sold'
		return self
		

	def addTax(self , num):
		self.price = self.price + (self.price * num)
		print self.price
		return self

	def returns(self):
		self.status = 'Disfunctional'
		self.price = 0
		return self

	def display(self):
		print self.item_name
		print self.weight
		print self.brand
		print self.status
		self.addTax(.12)


pro1 = product(10, 'watermelon', '2lbs', 'homegrown')
pro1.sell().display()
