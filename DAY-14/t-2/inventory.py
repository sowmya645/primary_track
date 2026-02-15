import json
from models import Product, Electronics, Grocery
from decorators import log_action

class InventoryIterator:
    def __init__(self, products):
        self._products = products
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._products):
            product = self._products[self._index]
            self._index += 1
            return product
        raise StopIteration


class Inventory:
    def __init__(self):
        self._products = []
        self.load()

    def __iter__(self):
        return InventoryIterator(self._products)

    @log_action
    def add_product(self, product):
        self._products.append(product)
        self.save()

    @log_action
    def remove_product(self, name):
        for p in self._products:
            if p.get_name().lower() == name.lower():
                self._products.remove(p)
                self.save()
                return
        raise Exception("Product not found")

    @log_action
    def update_stock(self, name, stock):
        for p in self._products:
            if p.get_name().lower() == name.lower():
                p.set_stock(stock)
                self.save()
                return
        raise Exception("Product not found")

    def search(self, name):
        for p in self._products:
            if name.lower() in p.get_name().lower():
                return p
        return None

    def get_all(self):
        return [p.get_details() for p in self._products]

    # JSON Persistence
    def save(self):
        with open("inventory.json", "w") as f:
            json.dump([p.get_details() for p in self._products], f, indent=4)

    def load(self):
        try:
            with open("inventory.json", "r") as f:
                data = json.load(f)
                for item in data:
                    if item["type"] == "Electronics":
                        product = Electronics(
                            item["name"], item["price"],
                            item["stock"], item["brand"]
                        )
                    elif item["type"] == "Grocery":
                        product = Grocery(
                            item["name"], item["price"],
                            item["stock"], item["expiry_date"]
                        )
                    else:
                        product = Product(
                            item["name"], item["price"],
                            item["stock"]
                        )
                    self._products.append(product)
        except FileNotFoundError:
            pass
