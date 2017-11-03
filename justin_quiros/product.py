class Product(object):
	
	def __init__(self, price, item_name, weight, brand, status="for sale"):
		self.price = price
		self.item_name =  item_name
		self.weight = weight 
		self.brand = brand
		self.status = status

	def sell(self):
		self.status = "sold"
		return self

	def add_tax(self, tax):
		self.price = round(self.price + (self.price*tax),2)
		return self

	def returns(self, reason):
		if reason == "defective":
			self.status = "defective"
			self.price = 0
		if reason == "like new":
			self.status = "for sale"
			self.price = round(self.price - (self.price * .20),2)
		return self

	def display_info(self):
		print "Price ${}".format(self.price)
		print "Item name: {}".format(self.item_name)
		print "Weight: {}".format(self.weight)
		print "Brand: {}".format(self.brand)
		print "Status: {}".format(self.status)
		return self


Potato = Product(2.13, "Potato", ".5 lbs", "Russet")
Banana = Product(1.13, "Banana", ".2 lbs", "Chiquita")
Chips = Product(2.99, "Chips", ".25 lbs", "Lays")
Salsa = Product(3.13, "Salsa", ".5 lbs", "Simply")
TV = Product(1999, "TV", "40 lbs", "LG")

# Potato.add_tax(.05)
# Potato.sell()
# # Potato.returns("defective")
# Potato.display_info()


# TV.returns("defective").display_info()
TV.add_tax(.06).sell().returns("like new").display_info()




