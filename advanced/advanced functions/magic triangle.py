def get_magic_triangle(n):
    matrix = [
        [1],
        [1,1],
    ]
    if n == 2:
        return matrix

    for _ in range(n-2):
        row = matrix[-1]
        next_row = []
        for i in range(len(row)):
            if i == 0:
                next_row.append(row[i])
            elif i == len(row) - 1:
                next_row.append(row[i] + row[i - 1])
                next_row.append(row[i])
            else:
                next_row.append(row[i] + row[i - 1])
        matrix.append(next_row)
    return matrix

get_magic_triangle(5)
