'''Product'''

class Product(object):
    def __init__(self, name, price, weight, brand, status = "for sale"):
        self.name = name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        self.status = "sold"
        return self

    def addTax(self, tax):
        self.price = self.price * (1 + tax)
        return self
    
    def returnProduct(self, reason):
        self.reason = reason
        if reason == "defective": self.price = 0
        elif reason == "box, like new": self.status = "for sale"
        elif reason == "box, opened": 
            self.status = "used"
            self.price = 0.8 * self.price #20% discount
        return self
    
    def display_info(self):
        print "Item Name: {}".format(self.name)
        print "Price: {}".format(self.price)
        print "Weight: {}".format(self.weight)
        print "Brand: {}".format(self.brand)
        print "Status: {}".format(self.status)
        return self

apple = Product("Apple", 10, "10 lb", "AppleCo")
apple.display_info()
apple.addTax(0.05)
apple.display_info()