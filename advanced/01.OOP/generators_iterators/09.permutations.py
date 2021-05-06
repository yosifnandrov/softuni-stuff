from itertools import permutations


def possible_permutations(some_list):
    possible_permutations = permutations(some_list, len(some_list))
    for permutation in possible_permutations:
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]