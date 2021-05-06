def read_matrix():
    row,col = [int(n) for n in input().split(", ")]
    matrix = [
        [int(el) for el  in input().split(", ")]
        for _ in range(row)
    ]
    return matrix
matrix = read_matrix()


def get_square(matrix):
    squares = []
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i]) - 1):
            square = [
                [matrix[i][j],matrix[i][j+1]],
                [matrix[i+1][j],matrix[i+1][j+1]]
                ]
            squares.append(square)
    return squares

def get_max_square(squares):
    max_sum = None
    for square in squares:
        current_sum = sum(square[0]) + sum(square[1])
        if max_sum is None or current_sum > max_sum:
            max_sum = current_sum
            max_square = square
    return max_square

squares = get_square(matrix)
max_square = get_max_square(squares)

print('\n'.join([" ".join(map(str,row)) for row in max_square]))
print(sum(max_square[0]) + sum(max_square[1]))


