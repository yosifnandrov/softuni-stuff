n = int(input())


def find_in_matrix(matrix, searched):
    for i, rows in enumerate(matrix):
        for j, symbol in enumerate(rows):
            if symbol == searched:
                return i, j

matrix = []

for _ in range(n):
    row = input()
    matrix.append(row)

searched = input()

pos = find_in_matrix(matrix,searched)

if pos:
    print(pos)
else:
    print(f"{searched} does not occur in the matrix")
