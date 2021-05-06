import sys

numbers = input().split()
n = int(input())
min_number = sys.maxsize
for i in range(n):
    for p in range(len(numbers)):
        numbers[p] = int(numbers[p])
        if numbers[p] < min_number:
            min_number = numbers[p]
    numbers.remove(min_number)
    min_number = sys.maxsize
print(numbers)
