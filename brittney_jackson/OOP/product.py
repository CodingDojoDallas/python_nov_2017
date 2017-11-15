

class Product(object):

	def __init__(self, Price, ItemName, Weight, Brand):
		self.Price = Price
		self.ItemName = ItemName
		self.Weight = Weight
		self.Brand = Brand
		self.Status = 'For Sale'
		#self.details()

	def sell(self):
		self.Status = 'Sold'
		return self

	def tax(self, tax):
		self.Price = (self.Price *tax) +self.Price
		return self.Price
		

	def returnItem(self, reason, Price):
		pass
		if reason == 'defective':
			self.Status = 'defective'
			self.Price = 0
		elif reason == 'open':
			self.Status = 'used'
			self.Price *= .8
		elif reason == 'like new':
			self.status = 'For Sale'
		return self
			

	def details(self):
		print "Item Name: " +str(self.ItemName)
		print "Price: " +str(self.Price)
		print "Item Weight: " +str(self.Weight)
		print "Brand Name: " +str(self.Brand)
		print "Status: " +str(self.Status)

lemons=Product(.25, 'Lemons', '.57 lbs', 'Sunshine')
spinach=Product(2.00, 'Spinach', '32 oz', 'Leafy Green')
salmon=Product(13.00, 'Salmon', '2 lbs', 'SeaFresh')
rice=Product(1.00, 'Rice', '2 lbs', 'Uncle Bens')
wine=Product(8.00, 'Wine', '750 ml', 'Box')

lemons.sell().tax(.08)
lemons.returnItem('defective', .25).details()







