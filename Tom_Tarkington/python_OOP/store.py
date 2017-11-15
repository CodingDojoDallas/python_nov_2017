global idcounter
idcounter = 1001

class Product(object):
    def __init__(self, pid, price, itemname, weight, brand, cost, status="for sale"):
        self.productid = pid
        global idcounter
        idcounter+=1
        self.price = price
        self.itemname = itemname
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
        self.id = id

    def display_info(self):
        print self.productid
        print self.price
        print self.itemname
        print self.weight
        print self.brand
        print self.cost
        print self.status
        print ""
        return self

    def sell(self):
        self.status = "sold"
        return self
        
    def AddTax(self, tax):
        self.price = round((tax*self.price),2)
        return self

    def Return(self, reason):
        if reason=="defective":
            self.status = "defective"
            self.price = 0
        elif reason=="returned in the box":
            self.status = "for sale"
        else:
            self.status = "used"
            self.price = self.price*.8
        return self


class Store(object):
    def __init__(self, owner, location):
        self.owner = owner
        self.address = location
        self.storeproducts = []

    # def __str__(self):
    #     if len(self.storeproducts) == 0:
    #         return "{}"
    #     return "{"+", ".join(str(e) for e in self.storeproducts) +"}"

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

item1 = Product(idcounter, 3.99, "ketchup", "38oz", "Heinz", 3.00)
item2 = Product(idcounter, 1.97, "Mustard", "20oz", "French's", 1.26)
item3 = Product(idcounter, 3.12, "Relish", "26oz", "Heinz", 2.66)

#item1.display_info()
#item2.display_info()

store1 = Store("Thomas Tarkington", "Dallas, TX")

print "*********************"
store1.add_product(item1).add_product(item2).inventory()
print "*********************"
store1.remove_product("ketchup").add_product(item3).inventory()