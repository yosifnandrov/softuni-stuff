product_data = input()
data_dict = {}
price_quantity = []
while not product_data == "buy":
    price_quantity.clear()
    name, price, quantity = product_data.split()
    price_quantity.append(float(price))
    price_quantity.append(int(quantity))
    if name not in data_dict:
        data_dict[name] = price_quantity.copy()
    elif name in data_dict:
        if not data_dict[name][0] == float(price):
            data_dict[name][0] = float(price)
        data_dict[name][1] += int(quantity)
    product_data = input()
def give_me_total(a,b):
    return f"{a*b:.2f}"
for item,value in data_dict.items():
    print(f"{item} -> {give_me_total(value[0], value[1])}")
