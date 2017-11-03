from store import Store
from product import Product

item1 = Product(3.99, "ketchup", "38oz", "Heinz", 3.00)
item2 = Product(1.97, "Mustard", "20oz", "French's", 1.26)
item3 = Product(3.12, "Relish", "26oz", "Heinz", 2.66)

store1 = Store("Thomas Tarkington", "Dallas, TX")
store2 = Store("Staci R", "Grand Prarire, TX")

print "*********************"
store1.add_product(item1).add_product(item2).inventory()
print "*********************"
store1.remove_product("ketchup").add_product(item3).inventory()