from collections import deque


def best_list_pureness(*args):
    rotations = args[-1]
    my_list = deque(args[:len(args)-1])
    total_pureness = 0
    for i in range(rotations):
        current_pureness = 0
        for j in range(len(my_list[0])):
            current_pureness += my_list[0][j] * j
        if current_pureness > total_pureness:
            total_pureness = current_pureness
            rotation = i
        deque(my_list[0]).rotate(1)
    return f"Best pureness {total_pureness} after {rotation} rotations"





test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)