numbers = input().split()
step = int(input())
new_list = []
counter = 0
for num in range(len(numbers)):
    numbers[num] = int(numbers[num])
while len(numbers) > 0:
    for s in range(len(numbers)):
        counter += 1
        if counter == step:
            new_list.append(numbers[s])
            numbers.remove(numbers[s])
            counter = 0
print(new_list)