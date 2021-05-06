from collections import deque

def create_matrix():
    rows,cols = [int(el) for el in input().split()]
    text = deque(list(input()))
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            letter = text.popleft()
            matrix[i].append(letter)
            text.append(letter)

    return matrix

matrix = create_matrix()
for i in range(len(matrix)):
    if i % 2 == 0:
        print(''.join(matrix[i]))
    else:
        print(''.join(matrix[i][::-1]))