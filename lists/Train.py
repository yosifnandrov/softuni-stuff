some_text = input()
wagons_list = some_text.split()
max_capacity = int(input())
add_passengers_wagons = input()


while not add_passengers_wagons == "end":
    if "Add" in add_passengers_wagons:
        passengers_list = add_passengers_wagons.split("Add ")
        passengers_str = "".join(passengers_list)
        passengers_str = int(passengers_str)
        wagons_list.append(passengers_str)
        add_passengers_wagons = input()
    else:
        passengers = int(add_passengers_wagons)
        for space in range(len(wagons_list)):
            wagons_list[space] = int(wagons_list[space])
            if wagons_list[space] + passengers <= max_capacity:
                wagons_list[space] += passengers
                break
        add_passengers_wagons = input()
        for space in range(len(wagons_list)):
            wagons_list[space] = str(wagons_list[space])
final_wagons = " ".join(wagons_list)
print(final_wagons)

#text = input()
# text_list = text.split()
#text_list[0] = ""
#text_str = ''.join(text_list)
#text_str = int(text_str)

#print(text_list)
#print(type(text_str))
#print(text_str)
