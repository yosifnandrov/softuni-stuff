n = int(input())
my_elements = set()
for _ in range(n):
    elements = input().split()
    for el in elements:
        my_elements.add(el)


for element in my_elements:
    print(element)