
from decorators.access import login_required
from shopping import items

cart = {}


def add_to_cart():
    while True:
        item = input("Enter item name: ")

        if item not in items:
            print(" Item not available")
            continue

        quantity = int(input("Enter quantity: "))
        cart[item] = quantity

        choice = input("Add more items? (YES/NO): ")
        if choice != "YES":
            break


def show_cart():
    print("\n Cart Items")
    for key, value in cart.items():
        print(f"Item: {key}  Quantity: {value}")
