import re

data = input()
furniture = []
total = 0
print("Bought furniture:")
while not data == "Purchase":
    pattern = r">>(?P<furniture>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)$"
    result = re.match(pattern,data, re.MULTILINE)
    if result:
        obj = result.groupdict()
        furniture.append(obj["furniture"])
        total += float(obj["price"]) * int(obj["quantity"])
    data = input()

for names in furniture:
    print(names)
print(f"Total money spend: {total:.2f}")

