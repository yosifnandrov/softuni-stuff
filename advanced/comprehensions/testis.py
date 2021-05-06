

my_dict = {x:x+1 for x in range(11)}
print(my_dict)

my_list = [1,2,3,4,5,6]
keys = my_list[::2]
values = my_list[1::2]

my_dict = dict(zip(keys,values))


print(my_dict)