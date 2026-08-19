sales = [
    {"product": "Laptop", "category": "Electronics", "price": 1200, "quantity": 2},
    {"product": "Mouse", "category": "Electronics", "price": 40, "quantity": 10},
    {"product": "Desk", "category": "Furniture", "price": 300, "quantity": 4},
    {"product": "Chair", "category": "Furniture", "price": 150, "quantity": 6},
    {"product": "Keyboard", "category": "Electronics", "price": 80, "quantity": 8},
]
for sale in sales:
    price = sale["price"]
    quantity = sale["quantity"]

    revenue = price * quantity

    print(f'{sale["product"]}: ${revenue}')