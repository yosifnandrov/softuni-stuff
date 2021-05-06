BOARD_SIZE = 8

matrix = [
    [el for el in input().split(" ")]
    for _ in range(BOARD_SIZE)
]


def find_king(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "K":
                king_position = (i,j)
                return king_position


def find_queen_horizontally(matrix, king_position):
    a,b = king_position
    for i in range(b, len(matrix[a]) - 1):
        if matrix[a][i+1] == "Q":
            first_queen = [a,i+1]
            return first_queen


def find_queen_horizontally_minus(matrix, king_position):
    a,b = king_position
    for i in range(b, - 1, -1):
        if matrix[a][i-1] == "Q":
            second_queen = [a,i-1]
            return second_queen


def find_queen_vertically_plus(matrix, king_position):
    a,b = king_position
    for i in range(a, len(matrix[a]) - 1):
        if matrix[i+1][b] == "Q":
            first_queen = [i+1,b]
            return first_queen


def find_queen_vertically_minus(matrix, king_position):
    a,b = king_position
    for i in range(a, 0, -1):
        if matrix[i-1][b] == "Q":
            first_queen = [i-1,b]
            return first_queen


def find_queen_diagonally(matrix,king_position):
    a, b = king_position
    for i in range(a, len(matrix[a]) - 1):
        if matrix[i + 1][b+1] == "Q":
            first_queen = [i + 1, b+1]
            return first_queen
        b += 1


def find_queen_diagonally_minus(matrix,king_position):
    a, b = king_position
    for i in range(a, 0, - 1):
        if matrix[i - 1][b-1] == "Q":
            first_queen = [i - 1, b-1]
            return first_queen
        b -= 1


queens = []

king_position = find_king(matrix)

queens.append(find_queen_horizontally(matrix,king_position))
queens.append(find_queen_vertically_plus(matrix,king_position))
queens.append(find_queen_horizontally_minus(matrix,king_position))
queens.append(find_queen_vertically_minus(matrix,king_position))
queens.append(find_queen_diagonally(matrix,king_position))
queens.append(find_queen_diagonally_minus(matrix,king_position))

queens = [el for el in queens if not el == None]
if queens:
    for el in queens:
        print(el)
else:
    print("The king is safe!")