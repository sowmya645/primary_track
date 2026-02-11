# shopping.py

items = {
    "apple": 30,
    "kurkure": 10,
    "pizza": 300,
    "momos": 200
}

def show_items():
    print("\n Available Items")
    for key, value in items.items():
        print(f"Item: {key}  Price: {value}")

        