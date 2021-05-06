#  coffee - 1.50
#  water - 1.00
#  coke - 1.40
#  snacks - 2.00
order = input()
count = int(input())
def bill(order, count):
    if order == "coffee":
        price = 1.5
        return (count * price)
    elif order == "water":
        price = 1.00
        return (count * price)
    elif order == "coke":
        price = 1.4
        return count * price
    elif order == "snacks":
        price = 2.00
        return count * price
result = bill(order, count)
print(f"{result:.2f}")