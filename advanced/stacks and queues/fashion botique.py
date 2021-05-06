box_stack = input().split()

capacity = int(input())
empty_rack = capacity
counter = 1
while len(box_stack) > 0:
    item = int(box_stack.pop())
    if capacity >= item:
        capacity -= item
    else:
        counter += 1
        capacity = empty_rack
        capacity -= item

print(counter)