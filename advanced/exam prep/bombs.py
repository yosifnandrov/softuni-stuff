matrix_size = int(input())
bombs = int(input())

matrix = [
    [0] * matrix_size
    for _ in range(matrix_size)
]

around = (
    (-1,0),
    (1,0),
    (0,-1),
    (0,1),
    (-1,-1),
    (-1,1),
    (1,1),
    (1,-1)

)

for _ in range(bombs):
    coords = input()
    i, j = eval(coords)
    matrix[i][j] = "*"
    for k, l in around:
        if 0 <= i + k <= len(matrix) - 1 and 0 <= j+l <= len(matrix) - 1:
            if not matrix[i+k][j+l] == "*":
                matrix[i+k][j+l] += 1


for row in matrix:
    print(' '.join(map(str, row)))


