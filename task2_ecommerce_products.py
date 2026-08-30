products = {
    "P001": {"name": "Laptop",  "category": "Electronics", "price": 1200, "quantity": 5},
    "P002": {"name": "Mouse",   "category": "Electronics", "price": 20,   "quantity": 0},
    "P003": {"name": "Desk",    "category": "Furniture",   "price": 150,  "quantity": 10},
    "P004": {"name": "Chair",   "category": "Furniture",   "price": 80,   "quantity": 0},
}


def lookup_product(product_id):
    return products.get(product_id)


def update_price(product_id, new_price):
    if product_id in products:
        products[product_id]["price"] = new_price
    else:
        print(f"Product {product_id} not found.")


def update_stock(product_id, new_quantity):
    if product_id in products:
        products[product_id]["quantity"] = new_quantity
    else:
        print(f"Product {product_id} not found.")


def get_out_of_stock_products():
    result = []
    for pid, details in products.items():
        if details["quantity"] == 0:
            result.append(pid)
    return result


print("Lookup P001:", lookup_product("P001"))

update_price("P002", 18)
print("\nAfter price update, P002:", lookup_product("P002"))

update_stock("P004", 25)
print("After stock update, P004:", lookup_product("P004"))

print("\nOut of stock products:", get_out_of_stock_products())
