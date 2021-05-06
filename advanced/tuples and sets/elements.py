first_num, second_num = tuple(int(x) for x in input().split(" "))


first = set()
second = set()
for _ in range(first_num):
    numbers_first = int(input())
    first.add(numbers_first)

for _ in range(second_num):
    numbers_second = int(input())
    second.add(numbers_second)

in_both = first.intersection(second)

for el in in_both:
    print(el)
