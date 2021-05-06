line = input()
new_list = []
new_dict = {}
while not line == "stop":
    new_list.append(line)
    line = input()

for i in range(0,len(new_list), 2):
    key = new_list[i]
    value = new_list[i+1]
    value = int(value)
    if key not in new_dict:
        new_dict[key] = value
    else:
        new_dict[key] += value

for key,value in new_dict.items():
    print(f"{key} -> {value}")

