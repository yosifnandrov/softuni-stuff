text = input()
n = int(input())

matrix = [
    [el for el in input()]
    for _ in range(n)
]

m = int(input())

movements = {
    "up": (-1,0),
    "down": (1,0),
    "left": (0,-1),
    "right": (0,1)
}


def get_current_position(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "P":
                current_position = (i,j)
                return current_position


def move(matrix, current_position, command):
    a,b = current_position
    x,y = command
    matrix[a][b] = "-"
    matrix[a+x][b+y] = "P"
    return matrix


def check_if_in_board(matrix, current_position, command):
    a,b = current_position
    x,y = command
    if (a+x >= 0 and a+x <= len(matrix)) and (b+y >= 0 and b+y <= len(matrix)):
        return True
    return False

def concatenate(text,matrix,current_position,command):
    i,j = current_position
    a,b = command
    new_position = matrix[i+a][j+b]
    if new_position.isalpha():
        text += new_position
        return text
    return text

for _ in range(m):
    command = input()
    current_position = get_current_position(matrix)
    if check_if_in_board(matrix,current_position,movements[command]):
        text = concatenate(text,matrix,current_position,movements[command])
        matrix = move(matrix,current_position,movements[command])
    else:
        if len(text) >= 1:
            text = text[:-1]

print(text)

for row in matrix:
    print("".join(row))