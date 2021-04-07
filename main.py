import store

zuh_shop = store.Store("Zuhayr's Odds and Ends")

print("")
print("Testing add product")

zuh_shop.add_product("table", 200, "furniture")
zuh_shop.add_product("chair", 50, "furniture")
zuh_shop.add_product("lamp", 25, "lights")
zuh_shop.add_product("flashlight", 5, "lights")
zuh_shop.add_product("apple", 1, "food")
zuh_shop.add_product("golden apple", 100, "food")

print("")

zuh_shop.list_products()

print("")
print("Testing sell product")
print("")

zuh_shop.sell_product("lamp")
zuh_shop.sell_product("flashlight")
zuh_shop.sell_product("pineapple")

print("")

zuh_shop.list_products()
zuh_shop.add_product("lamp", 25, "lights").add_product("flashlight", 5, "lights")

print("")
print("Testing inflation")
print("")
zuh_shop.list_products()
print("")
zuh_shop.inflation(.05)
print("")
zuh_shop.list_products()
print("")

print("Testing Sales")
zuh_shop.set_clearance(.05, "furniture")
print("")
zuh_shop.list_products()

print("")
print("Testing ID system")
print("")
zuh_shop.add_product("table", 200, "furniture")
zuh_shop.add_product("table", 200, "furniture")
zuh_shop.add_product("table", 200, "furniture")
zuh_shop.add_product("table", 200, "furniture")
print("")
zuh_shop.list_products()