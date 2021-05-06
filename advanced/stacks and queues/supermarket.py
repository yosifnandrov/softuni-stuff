from collections import deque

people = deque()
command = input()
while not command == "End":
    if command == "Paid":
        while len(people) > 0:
            print(people.popleft())

    else:
        name = command
        people.append(name)
    command = input()

print(f"{len(people)} people remaining.")

