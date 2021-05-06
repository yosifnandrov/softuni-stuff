wagons = int(input())
wagons_list = [0]*wagons
wagons_list = [int(el) for el in wagons_list]
command = input()
while not command == "End":
    command_list = command.split()
    if len(command_list) == 3:
        action = command_list[0]
        index = command_list[1]
        people = command_list[2]
        index = int(index)
        people = int(people)
    else:
        action = command_list[0]
        people = command_list[1]
        people = int(people)
    if action == "add":
        wagons_list[-1] += people
    elif action == "insert":
        wagons_list[index] += people
    elif action == "leave":
        wagons_list[index] -= people
    command = input()
print(wagons_list)
