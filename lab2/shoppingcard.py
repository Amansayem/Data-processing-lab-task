cart = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]

total = 0
for item in cart:
    total += item["price"] * item["quantity"]

if total >= 2000:
    discount = total * 0.10
else:
    discount = 0

final_price = total - discount

print("Total Cost:", total)
print("Discount Applied:", discount)
print("Final Price:", final_price)
