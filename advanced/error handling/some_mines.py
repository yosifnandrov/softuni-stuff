board = int(input())
mines = int(input())

matrix = [
    [0 for el in range(board)]
    for rows in range(board)
]

for _ in range(mines):
    k,l = eval(input())
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if k == i and j == l:
                matrix[i][j] = "*"






print(matrix)
