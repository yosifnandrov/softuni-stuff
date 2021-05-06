numbers = input().split(", ")
numbers = [int(x) for x in numbers]
even_list = []
for n in range(len(numbers)):
    if numbers[n] % 2 == 0:
        even_list.append(n)
print(even_list)


