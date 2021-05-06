from collections import deque

n = int(input())

commands = deque(input().split())
for i in range(len(commands)):
    if commands[i] == "up":
        commands[i] = (-1,0)
    elif commands[i] == "down":
        commands[i] = (1,0)
    elif commands[i] == "left":
        commands[i] = (0,-1)
    elif commands[i] == "right":
        commands[i] = (0,1)

matrix = [
    input().split()
    for _ in range(n)
]
up = (-1,0)
down = (1,0)
left = (0,-1)
right = (0,1)

movements = (
    up,
    down,
    left,
    right
)


total_coals = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "c":
            total_coals += 1

current_position = None
collected_coals = 0
counter_commands = 0
while commands:
    for i in range(len(matrix)):
        next_command = False
        for j in range(len(matrix[i])):
            if matrix[i][j] == "s" and counter_commands == 0:
                current_position = (i,j)
            if (i,j) == current_position:
                for command in commands:
                    for k,l in movements:
                        if command == (k,l):
                            commands.popleft()
                            counter_commands += 1
                            if 0 <= i+k <= len(matrix) - 1 and 0 <= j+l <= len(matrix[i]) - 1:
                                current_position = (i+k,j+l)
                            else:
                                next_command = True
                                break
                            if matrix[i+k][j+l] == "e":
                                print(f"Game over! ({i+k}, {j+l})")
                                exit()
                            elif matrix[i+k][j+l] == "c":
                                collected_coals += 1
                                matrix[i+k][j+l] = "*"
                                if collected_coals == total_coals:
                                    print(f"You collected all coals! ({i+k}, {j+l})")
                                    exit()
                                else:
                                    next_command = True
                                    break
                            next_command = True
                            break
                    if next_command:
                        break
                if next_command:
                    break
        if next_command:
            break

print(f"{total_coals - collected_coals} coals left. {current_position}")


