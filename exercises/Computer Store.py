prices = input()
parts = []
taxes = []
while not prices == "special" and not prices == "regular":
    prices = float(prices)
    if prices < 0:
        print("Invalid price!")
        prices = input()
    else:
        parts.append(prices)
        tax = prices * 0.2
        taxes.append(tax)
        prices = input()

for_parts = sum(parts)
for_taxes = sum(taxes)
total_price = for_taxes + for_parts
if total_price == 0:
    print(f"Invalid order!")
elif prices == "special":
    total_price -= total_price * 0.1
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {for_parts:.2f}$\nTaxes: {for_taxes:.2f}$\n-----------\nTotal price: {total_price:.2f}$")
else:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {for_parts:.2f}$\nTaxes: {for_taxes:.2f}$\n-----------\nTotal price: {total_price:.2f}$")




