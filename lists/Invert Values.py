number = input()
list_number = number.split()
for i in range(len(list_number)):
    list_number[i] = int(list_number[i])
opposite_list = [-x for x in list_number]
print(opposite_list)


