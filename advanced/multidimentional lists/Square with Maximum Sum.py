import numpy as np
import sys

rows, columns = [int(el) for el in input().split(", ")]
matrix = []
for i in range(rows):
    col = [int(el) for el in input().split(", ")]
    matrix.append(col)
max_sum = -sys.maxsize
matrix = np.array(matrix)
while True:
    i = 0
    j = 2
    while i <= rows - 2 and j <= rows:
        k = 0
        l = 2
        while k <= columns - 2 and l <= columns:
            a = matrix[i:j,k:l]
            if sum(sum(a)) > max_sum:
                max_sum = sum(sum(a))
                sub_matrix = a
            k += 1
            l += 1
        i += 1
        j += 1
    break

for array in range(len(sub_matrix)):
    for n in range(len(sub_matrix[array])):
        print(f"{sub_matrix[array][n]}", end=" ")
    print()
print(max_sum)

