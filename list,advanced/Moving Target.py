targets = input().split()
targets = [int(i) for i in targets]
command = input()

while not command == "End":
    action, index, value = command.split()
    index = int(index)
    value = int(value)
    if action == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
        else:
            command = input()
            continue
        if targets[index] <= 0:
            targets.pop(index)
    elif action == "Add":
        if index >= len(targets) or index < 0:
            print(f"Invalid placement!")
        else:
            targets.insert(index, value)
    elif action == "Strike":
        if len(targets) < index + value or index < value:
            print(f"Strike missed!")
            command = input()
            continue
        else:
            del targets[index-value:index+value+1]
    command = input()
targets = [str(i) for i in targets]
targets_as_str = "|".join(targets)
print(targets_as_str)