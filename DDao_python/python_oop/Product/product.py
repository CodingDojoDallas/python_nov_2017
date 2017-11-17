class Product(object):
	def __init__(self, price, item_name, weight, brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "For Sale"
		self.sell()
		self.add_tax()
		self.reason_for_return()
		self.display_info()

	def sell(self):
		if self.status == "For sale":
			self.status = "sold"

	def add_tax(self):
		sales_tax = 0.12 
		return self.price + sales_tax

	def reason_for_return(self):
		returns = "defective"
		box = "new"
		discount = "20%"
		if returns == "defective":
			self.status = returns
			self.price = 0
		elif box == "new": 
			self.status = "For Sale"
		else: box != "New"
		self.status = "Used " +  discount + " discount"

	def display_info(self):
		print "Price $" + str(self.price)
		print "Item Name: " + str(self.item_name)
		print "Weight: " + str(self.weight) + "lbs"
		print "Brand: " + str(self.brand)
		print "Status: " + str(self.status)

product1 = Product(.32, "Tomatos", .25, "Valley", )
product1.sell()
product1.add_tax()
product1.reason_for_return()
prodcut2 = Product(5.85, "Cheese", 2.4, "Velveeta")
product1.sell()
product1.add_tax()
product1.reason_for_return()