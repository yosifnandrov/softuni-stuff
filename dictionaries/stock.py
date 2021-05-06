my_products = input().split()
searched_products = input().split()
my_dict = {}
for i in range(0, len(my_products), 2):
    key = my_products[i]
    value = (my_products[i + 1])
    my_dict[key] = int(value)

for word in searched_products:
    if word in my_dict:
        print(f"We have {my_dict.get(word)} of {word} left")
    else:
        print(f"Sorry, we don't have {word}")

