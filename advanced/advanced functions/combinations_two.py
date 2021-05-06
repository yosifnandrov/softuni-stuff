from itertools import permutations

text = list(input())
r = len(text)

for comb in list(permutations(text,r)):
    print(''.join(comb))