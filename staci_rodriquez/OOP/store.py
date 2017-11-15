class Product(object):
	def __init__(self, price, ItemName, Weight, Brand, Cost, Status = "for sale"):
		self.price = price
		self.ItemName = ItemName
		self.Weight = Weight
		self.Brand = Brand
		self.Cost = Cost
		self.Status = Status

	def sell(self):
		self.Status = "sold"
		return self 

	def addTax(self, tax):
		self.price = round((self.price * self.tax),2)
		return self

	def returns(self, reason):
		if(reason == "defective"):
			self.Status = "Defective"
			self.price = 0

		elif(reason == "new"):
			self.Status = "for sale"

		else:
			self.Status = "used"
			self.price = self.price * .8
		return self

	def displayInfo(self):
		print self.price
		print self.ItemName
		print self.Weight
		print self.Brand
		print self.Cost
		print self.Status
		print "*************"
		return self

class Store(object):
	def __init__(self, location, owner):
		self.products = []
		self.location = location
		self.owner = owner
	
	def add_product(self, products):
		self.products.append(products)
		return self

	def remove_product(self, products):
		for x in self.products:
			if x.ItemName == products:
				self.products.remove(x)
		return self

	def inventory(self):
		for x in self.products:
			x.displayInfo()
		return self


store1 = Store(" Dallas, TX ", " Staci Rodriquez ")

product1 = Product(3.99, "Nail Polish", ".5 oz", "O.P.I", 1.35, "for sale")
product2 = Product(4.94, "Eyeliner", ".08 oz", "CoverGirl", 1.85, "for sale")
product3 = Product(5.99, "Lipstick", ".15 oz", "Maybelline", 2.05, "for sale")

store1.add_product(product1).add_product(product2).add_product(product3).remove_product("Nail Polish").inventory()