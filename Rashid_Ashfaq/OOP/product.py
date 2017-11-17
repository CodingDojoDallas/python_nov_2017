class Product(object):
    def __init__(self,price,item_name,weight,brand):
        self.price=price
        self.item_name=item_name
        self.brand=brand
        self.weight=weight
        self.status="for sale"

    def sellStatus(self):
        self.status="sold"

    def addTax(self,tax):
        self.price= self.price +tax
        return self.price

    def returnProduct(self,reason):
        if reason == "defective":
            self.status="defective"
            self.price=0
        elif reason == "in the box":
            self.status= "for sale"
        elif reason == "open box":
            self.status="used"
            self.price-=self.price*0.20

    def showallproduct(self):
        print "Product Price :", self.price
        print "Product Name :" ,self.item_name
        print "Product Weight:", self.weight
        print "Product.Brand:" , self.brand
        print "Product.status" , self.status

product1 = Product(650 ,"iPhone", "apple", "3pounds")
product1.showallproduct()
product1.addTax(3)
product1.returnProduct("open box")
product1.sellStatus()
