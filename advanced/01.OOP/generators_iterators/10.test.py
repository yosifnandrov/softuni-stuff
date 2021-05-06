from itertools import permutations
from collections import defaultdict

# a = [1,2,3]
#
# b = [10,9,8]
#
# for i,j in zip(a,b):
#     print(i,j)
#
#
# print(list(zip(a,b)))

# matrix = [
#     [0]*5
#     for _ in range(5)
# ]
#
# movements = list(permutations(range(-1,2),2))
# movements.append((1,1))
# movements.append((-1,-1))
# print(movements)
#
#
#
#
# matrix[2][2] = 8
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] == 8:
#             for move in movements:
#                 k,l = move
#                 matrix[i+k][j+l] = 1
#
#
# for row in matrix:
#     print(row)

#
# perm = [0, 0, 0]
# used = [False] * 3


# def possible_permutations(sequence, target_indx = 0):
#     if target_indx == len(sequence):
#         print(perm)
#         return
#
#     for i,x in enumerate(sequence):
#         if not used[i]:
#             perm[target_indx] = x
#             used[i] = True
#             possible_permutations(sequence, target_indx+1)
#             used[i] = False
#
#
# possible_permutations([1,2,3])


