def create_matrix():
    rows,cols = [int(el) for el in input().split()]
    matrix = [
        input().split()
        for _ in range(rows)
    ]
    return matrix

def swap_items(matrix,command):
    cmd,row,pos,row_two,pos_two = command.split()
    row = int(row)
    pos = int(pos)
    row_two = int(row_two)
    pos_two = int(pos_two)
    first = matrix[row][pos]
    second = matrix[row_two][pos_two]
    matrix[row][pos] = second
    matrix[row_two][pos_two] = first
    for row in matrix:
        print(' '.join(row))


def valid_command(command,matrix):
    command = command.split()
    if not command[0] == "swap":
        return False
    elif not len(command) == 5:
        return False
    for i in range(1,len(command) - 1):
        if i % 2 == 1:
            if int(command[i]) >= len(matrix):
                return False
        else:
            if int(command[i]) >= len(matrix[0]):
                return False
    else:
        return True

matrix = create_matrix()
command = input()

while not command == "END":
    if valid_command(command, matrix):
        swap_items(matrix,command)
    else:
        print("Invalid input!")
    command = input()


