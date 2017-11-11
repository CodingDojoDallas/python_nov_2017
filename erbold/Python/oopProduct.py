# OOP Product

# -Create a program to track products
# -Create a product class to fill the following requirements
# 	-Attributes:
# 		-price
# 		-item name
# 		-weight
# 		-brand
# 		-status: default 'for sale'
# 	-Methods:
# 		-Sell: changes status to "sold"
# 		-Add tax: takes tax as a decimal amount as a parameter and returns the price of 
# 		the item including sales tax
# 		-Return: takes reason for return as a parameter and changes status accordingly. 
# 		If the item is being returned because it is defective, change status to 'defective' 
# 		and change price to 0. If it is being returned in the box, like new, mark it 'for sale'. 
# 		If the box has been opened, set the status to 'used' and apply a 20% discount.
# 		-Display Info: show all product details
# 		-Every method that doesn't have to return something should return self so methods can be chained

# Pseudocode:

class Products(objects):

	def _init_(self, price, item_name, weight, brand, status):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = status

	def Display_Info(self):
		print self.price
			else return self
		print self.item_name
			else return self
		print self.weight
			else return self
		print self.brand
			else return self
		print self.status
			else return self

	def Sell(self):
		status = "sold"

	def Add_tax(self):
		self.price = price + (price * .08)

	def Return(self):
		if reason is "defective":
			self.status = "defective"
			self.price = 0

		elif reason is "in the box":
			self.status = "for sale"

		elif reason is "opened box":
			self.status = "used"
			self.price = price * .8

product1 = Products(60, 'Dope', '20lbs', 'Folgers')



