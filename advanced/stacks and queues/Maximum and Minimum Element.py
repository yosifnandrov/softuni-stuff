times = int(input())
stack = []

for i in range(times):
    command = input()
    if command == "2":
        if len(stack) > 0:
            stack.pop()
    elif command == "3":
        if len(stack) > 0:
            print(max(stack))
    elif command == "4":
        if len(stack) > 0:
            print(min(stack))
    else:
        first,second = command.split()
        stack.append(int(second))

print(', '.join(reversed([str(el) for el in stack])))
