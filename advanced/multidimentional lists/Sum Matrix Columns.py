rows,cols = [int(el) for el in input().split(", ")]

matrix = []
for i in range(rows):
    col = [int(el) for el in input().split()]
    matrix.append(col)

for j in range(cols):
    sum_cols = 0
    for i in range(rows):
        sum_cols += matrix[i][j]
    print(sum_cols)


