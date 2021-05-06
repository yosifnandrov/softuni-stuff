from collections import defaultdict

d = defaultdict(int)

numbers =[float(el) for el in input().split()]

for n in numbers:
    d[n] += 1

for number,count in d.items():
    print(f"{number} - {count} times")





