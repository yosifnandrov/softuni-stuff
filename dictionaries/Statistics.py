pairs = input()
my_dict = {}


while not pairs == "statistics":
    key,value = pairs.split(": ")
    value = int(value)
    if key not in my_dict:
        my_dict[key] = value
    else:
        my_dict[key] += value
    pairs = input()

print(f"Products in stock:")

for key,value in my_dict.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(my_dict)}")
print(f"Total Quantity: {sum(my_dict.values())}")
