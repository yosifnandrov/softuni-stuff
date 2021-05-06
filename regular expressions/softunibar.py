import re

order = input()
total_income = 0
while not order == "end of shift":
    pattern = r"(?<=^)\%(?P<name>[A-Z][a-z]+)\%([\w]+)?<(?P<product>[a-zA-Z]+)\>([\w]+)?\|(?P<quantity>\d+)\|([\w]+)?(?P<price>\d+(\.\d+)?)(?=\$)"
    valid_order = re.finditer(pattern,order)
    for _ in valid_order:
        purchase_price = float(_.groupdict()['price']) * int(_.groupdict()['quantity'])
        total_income += purchase_price
        print(f"{_.groupdict()['name']}: {_.groupdict()['product']} - {purchase_price:.2f}")
    order = input()
print(f"Total income: {total_income:.2f}")

