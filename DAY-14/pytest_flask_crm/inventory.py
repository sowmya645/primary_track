import json
import csv
from abc import ABC, abstractmethod
from functools import wraps

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id   
        self.__name = name
        self.__price = price
        self.__stock = stock

    
    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price

    def get_stock(self):
        return self.__stock

    def set_stock(self, stock):
        if stock < 0:
            raise ValueError("Stock cannot be negative")
        self.__stock = stock

    @abstractmethod
    def category(self):
        pass

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "category": self.category()
        }


class Electronics(Product):
    def category(self):
        return "Electronics"

class Grocery(Product):
    def category(self):
        return "Grocery"

class Inventory:
    def __init__(self):
        self.products = []

    @log_action
    def add_product(self, product):
        self.products.append(product)

    @log_action
    def remove_product(self, product_id):
        self.products = [p for p in self.products if p.get_id() != product_id]

    @log_action
    def update_stock(self, product_id, new_stock):
        for p in self.products:
            if p.get_id() == product_id:
                p.set_stock(new_stock)
                return
        raise Exception("Product not found")

    def search(self, keyword):
        return [p for p in self.products if keyword.lower() in p.get_name().lower()]

    
    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.products):
            result = self.products[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    
    @log_action
    def save_to_json(self, filename="inventory.json"):
        with open(filename, "w") as f:
            json.dump([p.to_dict() for p in self.products], f, indent=4)

    @log_action
    def load_from_json(self, filename="inventory.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.products = []
                for item in data:
                    if item["category"] == "Electronics":
                        self.add_product(Electronics(item["id"], item["name"], item["price"], item["stock"]))
                    elif item["category"] == "Grocery":
                        self.add_product(Grocery(item["id"], item["name"], item["price"], item["stock"]))
        except FileNotFoundError:
            print("No inventory file found, starting fresh.")

    @log_action
    def save_to_csv(self, filename="inventory.csv"):
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "name", "price", "stock", "category"])
            writer.writeheader()
            for p in self.products:
                writer.writerow(p.to_dict())


if __name__ == "__main__":
    inv = Inventory()
    inv.add_product(Electronics(1, "Laptop", 50000, 10))
    inv.add_product(Grocery(2, "Rice Bag", 1200, 50))
    inv.update_stock(1, 8)
    results = inv.search("Laptop")
    for r in results:
        print(f"Found: {r.get_name()} - Stock: {r.get_stock()}")
    for product in inv:
        print(product.to_dict())
    inv.save_to_json()
    inv.save_to_csv()
    inv.load_from_json()