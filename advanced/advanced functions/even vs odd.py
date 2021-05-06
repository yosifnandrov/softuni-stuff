command = input()

numbers = [int(el) for el in input().split()]

if command == "Odd":
    odd = [el for el in numbers if el % 2 == 1]
    res = sum(odd) * len(numbers)
    print(res)
elif command == "Even":
    even = [el for el in numbers if el % 2 == 0]
    res = sum(even) * len(numbers)
    print(res)