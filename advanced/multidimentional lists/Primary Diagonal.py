n = int(input())
matrix = []
for i in range(n):
    row = [int(el) for el in input().split()]
    matrix.append(row)

total_diagonal = 0

for i in range(n):
    total_diagonal += matrix[i][i]
print(total_diagonal)