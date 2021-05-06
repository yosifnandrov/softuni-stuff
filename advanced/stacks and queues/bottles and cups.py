from collections import deque

cups = input().split()
cups = deque([int(el) for el in cups])


bottles = (input().split())
bottles = [int(el) for el in bottles]
wasted = 0
while cups:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()
    if current_bottle < current_cup:
        current_cup -= current_bottle
        cups.appendleft(current_cup)
    elif current_bottle >= current_cup:
        wasted += current_bottle - current_cup
    if not bottles:
        print(f"Cups:", end=" ")
        while cups:
            if len(cups) == 1:
                print(cups.popleft())
            else:
                print(f'{cups.popleft()}', end=" ")
if bottles:
    print(f"Bottles:", end=" ")
    while bottles:
        if len(bottles) == 1:
            print(bottles.pop())
        else:
            print(f'{bottles.pop()}', end=" ")

print(f"Wasted litters of water: {wasted}")

