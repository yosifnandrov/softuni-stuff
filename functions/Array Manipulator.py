numbers_as_list = input().split()
numbers_as_list = [int(x) for x in numbers_as_list]
for n in numbers_as_list:
    if n % 2 == 0:
        print(n, end=" ")




