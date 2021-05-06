from collections import deque

quantity = int(input())
people = deque()
command = input()

while not command == "Start":
    name = command
    people.append(name)
    command = input() 

new_command = input()
while len(people) > 0:
    if new_command.isdigit():
        new_command = int(new_command)
        if quantity >= new_command:
            quantity -= new_command
            person = people.popleft()
            print(f"{person} got water")
        else:
            person = people.popleft()
            print(f"{person} must wait")
    elif "refill" in new_command:
        liters = new_command.split()[-1]
        liters = int(liters)
        quantity += liters
    else:
        break
    new_command = input()

print(f"{quantity} liters left")