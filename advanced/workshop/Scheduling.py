tasks = [int(el) for el in input().split(", ")]
n = int(input())

finished_cycles = []
for i in range(len(tasks)):
    if tasks[i] < tasks[n]:
        finished_cycles.append(tasks[i])
    elif tasks[i] == tasks[n]:
        if i <= n:
            finished_cycles.append(tasks[i])


print(sum(finished_cycles))

