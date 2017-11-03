#Assignment 3 Python OOP -Product
#Create a product class

class product(object):
	def __init__(self, price, name, brand, weight, ):
		self.price = price
		self.name = name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"

	def sell(self):
		self.status = "sold"

	def addTax(self, tax):
		self.price = self.price + ((self.price * tax)/100)
		return self.price

	def displayInfo(self):
		print "Item Brand: " + self.brand
		print "Item Name: " + self.name
		print "Item Price: " , self.price
		print "Item Weight: " , self.weight
		print "Item Status: " + self.status

	def returnx(self, reason):
		if reason == "defective":
			self.status = reason
			self.price = 0
		elif reason == "in the box":
			self.status = "for sale"
		elif reason == "opened":
			self.status = "used"
			self.price = self.price - (self.price * 0.20)

product1 = product(250, "Phone", "Samsung", "2pounds")
product1.displayInfo()
product1.addTax(10)
product1.displayInfo()
product1.returnx("defective")
product1.displayInfo()
product1.returnx("in the box")
product1.displayInfo()
product1.returnx("opened")
product1.displayInfo()