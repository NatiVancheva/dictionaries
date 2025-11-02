stock_data = input().split()
product_to_search = input().split()
stock = {}

for i in range(0, len(stock_data), 2):
    product = stock_data[i]
    quantity = stock_data[i + 1]
    stock[product] = quantity

for product in product_to_search:
    if product in stock:
        print(f'We have {stock[product]} of {product} left.')
    else:
        print(f"Sorry, we don\n't have {product}.")