'''
Imagine a small store inventory like {"apple": 10, "banana": 5, "milk": 2}. Program should allow
adding new items, selling items (subtract quantity), and print items that are low in stock (<3).
'''

store = {
    "apple": 10,
    "banana": 5,
    "milk": 2
}

def add_items(item, quantity):
    item = item.lower()
    if(quantity>0):
        store[item] = store.get(item, 0) + quantity
    else:
        print("Please insert a positive integer")


def sell_items(item, quantity=1):
    items = item.lower()
    if(items not in store):
        print(f"{item} not found in Store")
        return

    if(store[item] >= quantity and quantity > 0 ):
        store[items] -= quantity
    elif (quantity <= 0):
        print("The quantity should be positive")
    else:
        print(f"You are trying to sell {quantity - store[item] } items more than how much in current stock")

    return

def low_stock():
    for name, quantity in store.items():
        if(quantity < 3):
            print(f"{name.capitalize()} is low on stocks. Quantity: {quantity}")

def print_store():
    for name, quantity in store.items():
        print(f"{name}: {quantity}")


add_items("apple",3)
print_store()
sell_items("banana")
print_store()
low_stock()
