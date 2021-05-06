import sys
def get_matrix():
    rows,cols = [int(el) for el in input().split()]
    matrix = [
        [int(el) for el in input().split()]
        for _ in range(rows)
    ]
    return matrix

def find_three_by_three_squares(matrix):
    squares = []
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[i]) - 2):
            square = [
                [matrix[i][j], matrix[i][j+1], matrix[i][j+2]],
                [matrix[i+1][j], matrix[i+1][j+1],matrix[i+1][j+2]],
                [matrix[i+2][j],matrix[i+2][j+1],matrix[i+2][j+2]]
            ]
            squares.append(square)
    return squares

def find_biggest_square(squares):
    biggest_sum = -sys.maxsize
    for square in squares:
        current_sum = 0
        for i in range(len(square)):
            current_sum += sum(square[i])
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            my_square = square
    return my_square

matrix = get_matrix()
squares = find_three_by_three_squares(matrix)
biggest_square = find_biggest_square(squares)
sum_square = 0
for square in biggest_square:
    sum_square += sum(square)

print(f"Sum = {sum_square}")
print('\n'.join(' '.join([str(el) for el in row]) for row in biggest_square))