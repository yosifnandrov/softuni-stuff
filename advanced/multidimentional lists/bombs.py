n = int(input())

matrix = [
    [int(el) for el in input().split()]
    for _ in range(n)
]

positions = (
    input().split()
)
for k in range(len(positions)):
    x, y = positions[k].split(",")
    x = int(x)
    y = int(y)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if x == i and j == y:
                if matrix[i][j] <= 0:
                    continue
                else:
                    moves = (
                        (0,1),
                        (0,-1),
                        (-1,-1),
                        (-1,0),
                        (-1,1),
                        (1,-1),
                        (1,0),
                        (1,1)
                    )
                    for l, m in moves:
                        if 0 <= i+l <= len(matrix) - 1 and 0 <= j+m <= len(matrix[i]) - 1:
                            if matrix[i+l][j+m] <= 0:
                                continue
                            else:
                                matrix[i+l][j+m] -= matrix[i][j]
                    matrix[i][j] = 0
counter = 0
total_sum = 0
for r in range(len(matrix)):
    for v in range(len(matrix[r])):
        if matrix[r][v] > 0:
            counter += 1
            total_sum += matrix[r][v]
print(f"Alive cells: {counter}")
print(f"Sum: {total_sum}")



for row in matrix:
    row = [str(el) for el in row]
    print(' '.join(row))


