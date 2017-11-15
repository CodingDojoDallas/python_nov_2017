class Product(object):
	def __init__(self, price, item_name, weight, brand, status="for sale"):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = status	

	def Sell(self):
		self.status = sold
		return self

	def AddTax(self):
		self.tax += self.price
		return self

	def Return(self):
		if self.status == "defective":
			self.price = 0
		elif self.status == "in the box":
			self.status = "for sale"
		elif self.status == "box is open":
			self.price *= 00.80
		return self

	def DisplayInfo(self):
		print " The price of this: {} {} is ${}, it weighs {} and it is {}".format(self.brand, self.item_name, 
			self.price, self.weight, self.status)

product1 = Product(19.99, "sweater", "10 oz", "Addidas", "box is open").Return().DisplayInfo()