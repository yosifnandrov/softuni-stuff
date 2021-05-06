import itertools

numbers = input().split(", ")
n = len(numbers)
permutations = set(itertools.permutations(["-"] * n + ["+"] * n, n))

for permutation in permutations:
    expr = "".join(itertools.chain(*zip(permutation, numbers)))
    print(f"{expr}={eval(expr)}")


# list_one = [1,2,3,4,5]
# list_one = [str(el) for el in list_one]
# list_two = ["-","/","*","-","+"]
#
# list_three = ' '.join(((itertools.chain(*zip(list_two,list_one)))))
# print(list_three)
#
# list_five = list(zip(list_two,list_one))
# list_four = ' '.join(list(itertools.chain(*list_five)))
# print(list_four)
# print(list_five)