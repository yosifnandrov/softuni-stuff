electrons = int(input())
levels = []
i = 1
per_index = lambda x: 2 * (x * x)
while electrons > 0:
    if electrons >= per_index(i):
        levels.append(per_index(i))
        electrons -= per_index(i)
        i += 1
    else:
        levels.append(electrons)
        electrons = 0
print(levels)