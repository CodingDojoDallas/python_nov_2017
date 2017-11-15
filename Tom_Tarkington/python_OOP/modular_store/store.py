class Store(object):
    def __init__(self, owner, location):
        self.owner = owner
        self.address = location
        self.storeproducts = []

    def add_product(self, itemname):
        self.storeproducts.append(itemname)
        return self

    def inventory(self):
        for x in self.storeproducts:
            x.display_info()
        return self
    
    def remove_product(self, productname):
        for x in self.storeproducts:
            if x.itemname == productname:
                self.storeproducts.remove(x)
        return self


# store1 = Store("Thomas Tarkington", "Dallas, TX")
# store2 = Store("Staci R", "Grand Prarire, TX")

