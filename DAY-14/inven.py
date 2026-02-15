import json
from functools import wraps

# -----------------------------
# DECORATOR FOR LOGGING
# -----------------------------

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Executing: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Completed: {func.__name__}\n")
        return result
    return wrapper


# -----------------------------
# BASE CLASS
# -----------------------------

class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    # Getters
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    # Setters
    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price

    def set_stock(self, stock):
        if stock < 0:
            raise ValueError("Stock cannot be negative")
        self.__stock = stock

    # Polymorphism
    def get_details(self):
        return {
            "type": "Product",
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }


# -----------------------------
# SUBCLASSES
# -----------------------------

class Electronics(Product):
    def __init__(self, name, price, stock, brand):
        super().__init__(name, price, stock)
        self.__brand = brand

    def get_details(self):
        details = super().get_details()
        details["type"] = "Electronics"
        details["brand"] = self.__brand
        return details


class Grocery(Product):
    def __init__(self, name, price, stock, expiry_date):
        super().__init__(name, price, stock)
        self.__expiry_date = expiry_date

    def get_details(self):
        details = super().get_details()
        details["type"] = "Grocery"
        details["expiry_date"] = self.__expiry_date
        return details


# -----------------------------
# CUSTOM ITERATOR
# -----------------------------

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


# -----------------------------
# INVENTORY CLASS
# -----------------------------

class Inventory:
    def __init__(self):
        self._products = []

    def __iter__(self):
        return InventoryIterator(self._products)

    @log_action
    def add_product(self, product):
        self._products.append(product)

    @log_action
    def remove_product(self, name):
        for p in self._products:
            if p.get_name().lower() == name.lower():
                self._products.remove(p)
                return
        raise Exception("Product not found")

    @log_action
    def update_stock(self, name, new_stock):
        for p in self._products:
            if p.get_name().lower() == name.lower():
                p.set_stock(new_stock)
                return
        raise Exception("Product not found")

    def search_product(self, name):
        for p in self._products:
            if name.lower() in p.get_name().lower():
                return p
        return None

    # -------------------------
    # FILE PERSISTENCE
    # -------------------------

    def save_to_file(self, filename="inventory.json"):
        data = [p.get_details() for p in self._products]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename="inventory.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for item in data:
                    if item["type"] == "Electronics":
                        product = Electronics(
                            item["name"],
                            item["price"],
                            item["stock"],
                            item["brand"]
                        )
                    elif item["type"] == "Grocery":
                        product = Grocery(
                            item["name"],
                            item["price"],
                            item["stock"],
                            item["expiry_date"]
                        )
                    else:
                        product = Product(
                            item["name"],
                            item["price"],
                            item["stock"]
                        )
                    self._products.append(product)
        except FileNotFoundError:
            pass


# -----------------------------
# MAIN PROGRAM (CMD INTERFACE)
# -----------------------------

def main():
    inventory = Inventory()
    inventory.load_from_file()

    while True:
        print("\n===== INVENTORY SYSTEM =====")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. View All Products")
        print("6. Save & Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                ptype = input("Type (1-Electronics, 2-Grocery): ")
                name = input("Name: ")
                price = float(input("Price: "))
                stock = int(input("Stock: "))

                if ptype == "1":
                    brand = input("Brand: ")
                    product = Electronics(name, price, stock, brand)
                else:
                    expiry = input("Expiry Date: ")
                    product = Grocery(name, price, stock, expiry)

                inventory.add_product(product)

            elif choice == "2":
                name = input("Product name to remove: ")
                inventory.remove_product(name)

            elif choice == "3":
                name = input("Product name: ")
                stock = int(input("New stock: "))
                inventory.update_stock(name, stock)

            elif choice == "4":
                name = input("Search name: ")
                product = inventory.search_product(name)
                if product:
                    print(product.get_details())
                else:
                    print("Not found")

            elif choice == "5":
                for p in inventory:
                    print(p.get_details())

            elif choice == "6":
                inventory.save_to_file()
                print("Saved. Exiting...")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
