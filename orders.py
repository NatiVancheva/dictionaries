products = {}

while True:
    command = input()
    if command == "buy":
        break
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products:
        products[name] = [price, quantity]
    else:
        products[name][0] = price
        products[name][1] += quantity

for name, values in products.items():
    total_price = values[0] * values[1]
    print(f"{name} -> {total_price:.2f}")

