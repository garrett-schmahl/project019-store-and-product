class Product:
  def __init__(self, name, price, category, id):
    self.name = name
    self.id = id
    self.price = price
    self.category = category
  

  def update_price(self, percent_change,is_increased):
    if is_increased:
      self.price = self.price + self.price*percent_change
    else:
      self.price = self.price - self.price*percent_change
    return self


  def print_info(self):
    print(f"{self.name} ID:{self.id}, {self.category}, ${self.price:.2f}")
    return self

