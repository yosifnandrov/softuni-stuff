numbers = input().split(", ")
new_list = []
counter = 0
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    if numbers[i] == 0:
        counter += 1
    else:
        new_list.append(numbers[i])
for zero in range(counter):
    new_list.append(0)

print(new_list)