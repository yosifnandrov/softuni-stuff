n = int(input())
matrix = [
    [el for el in input().split(", ")]
    for _ in range(n)
]

matrix = [int(num) for row in matrix for num in row]

print(matrix)