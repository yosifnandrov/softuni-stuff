from collections import deque


males = [int(el) for el in input().split() if int(el) > 0]
females = deque([int(el) for el in input().split() if int(el) > 0])
matches = 0

while females:
    female = females.popleft()
    male = males.pop()
    if female == male:
        matches += 1
    else:
        males.append(male)
        males[-1] -= 2
        if males[-1] <= 0:
            males.pop()
        elif males[-1] % 25 == 0:
            if len(males) > 1:
                males.pop()
                males.pop()
            else:
                males.pop()
    if not males:
        break

print(f"Matches: {matches}")
if males:
    males = reversed(males)
    print(f"Males left: {', '.join(map(str, males))}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print(f"Females left: none")

