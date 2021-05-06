from collections import deque


def list_manipulator(some_list, *args):
    some_list = deque(some_list)
    command, position, *values = args
    if command == "remove":
        if position == "end":
            if values:
                for _ in range(values[0]):
                    some_list.pop()
            else:
                some_list.pop()
        elif position == "beginning":
            if values:
                for _ in range(values[0]):
                    some_list.popleft()
            else:
                some_list.popleft()
    elif command == "add":
        if position == "end":
            for i in range(len(values)):
                some_list.append(values[i])
        elif position == "beginning":
            for i in range(len(values) -1 ,-1,-1):
                some_list.appendleft(values[i])
    return list(some_list)


print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))