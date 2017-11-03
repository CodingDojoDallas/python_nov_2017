class Product(object):
	def __init__(self,price,name,weight,brand):
		self.price=price
		self.name=name
		self.weight=weight
		self.brand=brand
		self.status="for sale"
		self.tax=0
		self.totalprice = self.price+self.price*self.tax
	def sell(self):
		self.status="sold"
		return self
	def addtax(self,rate):
		self.tax = rate
		self.totalprice = self.price+self.price*self.tax
		print ("Price with tax is: $" + str(self.totalprice))
		return self
	def return_item(self, reason):
		self.reason = reason
		if self.reason=="defective":
			self.status="defective"
			self.price=0
		elif self.reason=="new":
			self.status="for sale"
		elif self.reason=="opened":
			self.status="used"
			self.price*=.8
		return self
	def display_info(self):
		print "Price: $"+str(self.price)
		print "Name: "+self.name
		print "Weight: "+self.weight
		print "Brand: "+self.brand
		print "Status: "+self.status
		print "Total price: $"+str(self.totalprice)

ball=Product(10,"football", "2kg", "nike")
ball.addtax(.1)
ball.display_info()


