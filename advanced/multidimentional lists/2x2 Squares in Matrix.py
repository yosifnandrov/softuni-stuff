def create_matrix():
    rows,cols = [int(el) for el in input().split()]
    matrix = [
        input().split()
         for _ in range(rows)
    ]
    return matrix

def get_two_by_two_squares(matrix):
    squares = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            square = [matrix[i][j], matrix[i][j+1],
                      matrix[i+1][j], matrix[i+1][j+1]]
            squares.append(square)
    return squares

def count_same_squares(squares):
    counter = 0
    for square in squares:
        if len(set(square)) == 1:
            counter += 1
    return counter

matrix = create_matrix()
squares = get_two_by_two_squares(matrix)
count = count_same_squares(squares)

print(count)
