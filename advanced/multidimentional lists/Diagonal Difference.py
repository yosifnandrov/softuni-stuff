def form_matrix():
    rows = int(input())
    matrix = [
        [int(el) for el in input().split()]
        for _ in range(rows)
    ]
    return matrix

def get_diagonals(matrix):
    first_diagonal = []
    second_diagonal = []
    for i in range(len(matrix)):
        first_diagonal.append(matrix[i][i])
    for j in range(len(matrix) - 1, -1, -1):
        second_diagonal.append(matrix[::-1][j][j])

    return [first_diagonal,second_diagonal]

def find_absolute_diff(diagonals):
    diff = abs(sum(diagonals[0]) - sum(diagonals[1]))
    return diff



matrix = form_matrix()
diagonals = get_diagonals(matrix)
diff = find_absolute_diff(diagonals)
print(diff)


