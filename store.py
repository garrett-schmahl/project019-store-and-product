import product
import random

class Store:
  def __init__(self, name):
    self.name = name
    self.products = {}


  def add_product(self, new_product, new_product_price, new_product_category):
    new_product_id = random.randrange(100000,999999,1)
    self.products[new_product+str(new_product_id)] = product.Product(new_product, new_product_price, new_product_category, new_product_id)
    print(f"Stocked {new_product} ID:{new_product_id}")
    return self

  
  def sell_product(self, sold_product):
    for product in self.products:
      product_exists = product.find(sold_product)
      if product_exists != -1:
        self.products.pop(product, None)
        print(f"Sold {sold_product}")
        return self
    return error(sold_product)
  

  def inflation(self, percent_increase):
    for product in self.products:
      self.products[product].update_price(percent_increase, True)
    print(f"prices inflated by {percent_increase*100}%")


  def set_clearance(self, percent_decrease, category):
    for product in self.products:
      if self.products[product].category == category:
        self.products[product].update_price(percent_decrease, False)


  def list_products(self):
    for product in self.products:
      self.products[product].print_info()

def error(err_product):
  print(f"Error, {err_product} does not exist")
  return False