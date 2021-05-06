numbers = input().split(",")
beggars = int(input())
beggars_list = []
counter = 0
finish_beggars = False

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

if len(numbers) == beggars:
    print(numbers)
elif beggars > len(numbers):
    for i in range(beggars):
        if i >= len(numbers):
            beggars_list.append(0)
        else:
            beggars_list.append(numbers[i])
    print(beggars_list)
elif beggars < len(numbers):
    for p in range(1, len(numbers) + 1):
        if p % (beggars + 1) == 0:
            finish_beggars = True
        if finish_beggars:
            beggars_list[counter] += numbers[p - 1]
            counter += 1
            if counter == beggars:
                counter = 0
        else:
            beggars_list.append(numbers[p - 1])
    print(beggars_list)


















