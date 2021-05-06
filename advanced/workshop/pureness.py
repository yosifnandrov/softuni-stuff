from collections import deque

def best_list_pureness(some_list, k_rotations):
    total_sum = 0
    some_list = deque(some_list)
    if len(some_list) == 1:
        return f"Best pureness 0 after 0 rotations"
    for rotations in range(k_rotations + 1):
        current_sum = 0
        for i in range(len(some_list)):
            current_sum += some_list[i] * i
        if current_sum > total_sum:
            total_sum = current_sum
            rots = rotations
        some_list.rotate(1)
    return f"Best pureness {total_sum} after {rots} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)