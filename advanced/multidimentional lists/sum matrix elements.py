rows, col = [int(el) for el in input().split(", ")]
total = 0
matrix = []
for i in range(rows):
    number = [int(el) for el in input().split(", ")]
    total += sum(number)
    matrix.append(number)
print(total)
print(matrix)