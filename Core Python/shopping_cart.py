class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.cart = []

    # Add items to cart
    def add_item(self, item):
        self.cart.append(item)
        print(f"{item.name} added to cart")

    # Remove item from the cart using item_name
    def remove_item(self, item_name):
        for item in self.cart:
            if item.name == item_name:
                self.cart.remove(item)
                print(f"{item.name} removed from the cart")
                return
        print("Item not found in the cart")

    # View all cart items
    def view_cart(self):
        if not self.cart:
            print("Cart is empty")
            return
        
        print("\n---- Cart Items ----")
        for item in self.cart:
            print(f"Name: {item.name}, Price: {item.price}, Quantity: {item.quantity}")

    # Total amount calculation
    def total_amount(self):
        total = 0
        for item in self.cart:
            total += item.price * item.quantity

        return total


cart = ShoppingCart()
item1 = Item("watch", 5000, 1)
item2 = Item("mobile", 10000, 2)

cart.add_item(item1)
cart.add_item(item2)

cart.view_cart()
print("Total Amount:", cart.total_amount())

cart.remove_item("mobile")
cart.view_cart()

