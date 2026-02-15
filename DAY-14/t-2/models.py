# OOP + Inheritance + Encapsulation + Polymorphism

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


class Electronics(Product):
    def __init__(self, name, price, stock, brand):
        super().__init__(name, price, stock)
        self.__brand = brand

    def get_details(self):
        data = super().get_details()
        data["type"] = "Electronics"
        data["brand"] = self.__brand
        return data


class Grocery(Product):
    def __init__(self, name, price, stock, expiry_date):
        super().__init__(name, price, stock)
        self.__expiry_date = expiry_date

    def get_details(self):
        data = super().get_details()
        data["type"] = "Grocery"
        data["expiry_date"] = self.__expiry_date
        return data
