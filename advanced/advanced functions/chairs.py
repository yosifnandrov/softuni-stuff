from itertools import combinations


names = input().split(", ")
chairs = int(input())

for comb in list(combinations(names,chairs)):
    print(", ".join(comb))
