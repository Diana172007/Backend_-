class Product :
    def __init__(self,price,quantity_in_stock,category):
        self.price=price
        self.quantity_in_stock=quantity_in_stock
        self.category=category
    def is_available(self, quantity):
        return self.quantity_in_stock>=quantity
    def reduce_stock(self, quantity):
        if self.is_available(quantity):
            self.quantity_in_stock=self.quantity_in_stock-quantity
            return self.quantity_in_stock
        else:
            return "на складе товара меньше"
class ShoppingCart(Product):
    pass
