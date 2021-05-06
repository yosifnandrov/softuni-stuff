elements = input().split()
my_dict = {}
elements = [i.lower() for i in elements]
for el in elements:
    key = el
    value = elements.count(el)
    my_dict[key] = value

for k in my_dict:
    if not my_dict[k] % 2 == 0:
        print(k, end=" ")
print()
print(my_dict)