key_value_list = input().split()
my_dict = {}

for i in range(0, len(key_value_list), 2):
    my_dict[key_value_list[i]] = int(key_value_list[i+ 1])
print(my_dict)

