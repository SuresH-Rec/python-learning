products = [
    {"name": "Laptop", "price": 55000, "qty": 1},
    {"name": "Keyboard", "price": 2500, "qty": 2},
    {"name": "Mouse", "price": 800, "qty": 3},
    {"name": "Monitor", "price": 12000, "qty": 2},
    {"name": "Headset", "price": 1500, "qty": 1},
    {"name": "Bluetooth Device", "price": 750, "qty": 4}
]

def calculate_total(price, qty):
    return price * qty


def shopping_category(total):
    if total >= 50000:
        return "Premium"
    elif total >= 20000:
        return "Expensive"
    elif total >= 5000:
        return "Standard"
    else:
        return "Budget"


grand_total = 0

print("Product Details")
print("-" * 20)

for product in products:
    total = calculate_total(product["price"], product["qty"])
    product["total"] = total
    grand_total += total

    print(f"Name  : {product['name']}")
    print(f"Price : {product['price']}")
    print(f"Qty   : {product['qty']}")
    print(f"Total : {product['total']}")
    print("-" * 20)

print("Grand Total =", grand_total)

category = shopping_category(grand_total)
print("Shopping Category =", category)
