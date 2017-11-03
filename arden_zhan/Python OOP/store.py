'''Store (optional)'''
class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
    
    def add_product(self, newProduct):
        self.products.append(newProduct)
        return self
    
    def remove_product(self, remProduct):
        self.products.remove(remProduct)
        return self
    
    def inventory(self):
        print "Products: {}".format(self.products)
        print "Location: {}".format(self.location)
        print "Owner: {}".format(self.owner)

store1 = Store(["thing1", "thing2"], "123 Street", "Owner of store 1")
store1.inventory()
store1.remove_product("thing1").inventory()
store1.add_product("testy3").inventory()