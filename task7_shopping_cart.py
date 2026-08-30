cart = {}


def add_to_cart(product_name, price, quantity=1):
    if product_name in cart:
        cart[product_name]["quantity"] += quantity
    else:
        cart[product_name] = {"price": price, "quantity": quantity}


def remove_from_cart(product_name):
    if product_name in cart:
        del cart[product_name]
    else:
        print(f"{product_name} is not in the cart.")


def update_quantity(product_name, new_quantity):
    if product_name in cart:
        cart[product_name]["quantity"] = new_quantity
    else:
        print(f"{product_name} is not in the cart.")


def calculate_total():
    total = 0
    for item in cart.values():
        total += item["price"] * item["quantity"]
    return total


add_to_cart("Laptop", 1200, 1)
add_to_cart("Mouse", 20, 2)
add_to_cart("Mouse", 20, 1)

print("Cart contents:")
for name, details in cart.items():
    print(f"  {name}: {details}")

update_quantity("Laptop", 2)
print("\nAfter updating Laptop quantity to 2:")
print("  Laptop:", cart["Laptop"])

remove_from_cart("Mouse")
print("\nAfter removing Mouse, cart contents:", cart)

print(f"\nTotal price: ${calculate_total()}")
