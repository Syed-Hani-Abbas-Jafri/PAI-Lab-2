 
products = {
    "P001": {"name": "Laptop", "category": "Electronics", "price": 1200, "quantity": 5},
    "P002": {"name": "Mouse", "category": "Electronics", "price": 20, "quantity": 0},
    "P003": {"name": "Desk", "category": "Furniture", "price": 150, "quantity": 3},
}
 
def lookup_product(product_id):
    return products.get(product_id)
 
def update_price(product_id, new_price):
    if product_id in products:
        products[product_id]["price"] = new_price
        return True
    return False
 
def update_stock(product_id, new_quantity):
    if product_id in products:
        products[product_id]["quantity"] = new_quantity
        return True
    return False
 
def out_of_stock_products():
    return [pid for pid, info in products.items() if info["quantity"] == 0]
 
print("Lookup P001:", lookup_product("P001"))
update_price("P001", 1100)
update_stock("P002", 10)
print("After updates:", products["P001"], products["P002"])
print("Out of stock now:", out_of_stock_products())
