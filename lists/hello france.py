collection = input().split("|")
budget = float(input())
new_prices = []
profit = 0
for items in collection:
    new_price = 0
    type_product, value = items.split("->")
    value = float(value)
    if type_product == "Clothes" and value > 50:
        continue
    elif type_product == "Shoes" and value > 35:
        continue
    elif type_product == "Accessories" and value > 20.50:
        continue
    if budget >= value:
        budget -= value
        new_price += value + (value * 0.4)
        new_prices.append(new_price)
        profit += value * 0.4
    else:
        continue
budget += sum(new_prices)
for el in new_prices:
    print(f"{el:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget >= 150:
    print(f"Hello, France!")
else:
    print("Time to go.")

