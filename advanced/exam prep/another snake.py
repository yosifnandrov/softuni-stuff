board_rows = int(input())

food = 0

matrix = [
    [el for el in input()]
    for _ in range(board_rows)
]

movements = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


def find_snake(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "S":
                snake_position = (i, j)
                return snake_position


def find_burrow(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "B":
                return i, j


command = input()

while True:
    i, j = find_snake(matrix)
    x, y = movements[command]
    if 0 <= i+x <= len(matrix) - 1 and 0 <= j+y <= len(matrix) - 1:
        if matrix[i+x][j+y] == "*":
            matrix[i][j] = "."
            matrix[i+x][j+y] = "S"
            food += 1
            if food >= 10:
                print("You won! You fed the snake.")
                break
        elif matrix[i+x][j+y] == "-":
            matrix[i][j] = "."
            matrix[i+x][j+y] = "S"
        elif matrix[i+x][j+y] == "B":
            matrix[i][j] = "."
            matrix[i+x][j+y] = "."
            a,b = find_burrow(matrix)
            matrix[a][b] = "S"
    else:
        matrix[i][j] = "."
        print("Game over!")
        break

    command = input()


print(f"Food eaten: {food}")

for row in matrix:
    print(f"{''.join(row)}")

