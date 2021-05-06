numbers = input()
list_numbers = numbers.split()
command = input()

while not command == "End":
    if "Add" in command:
        command_list = command.split()
        list_numbers.append(command_list[1])
    elif "Insert" in command:
        command_list = command.split()
        command_list[1] = int(command_list[1])
        command_list[2] = int(command_list[2])
        list_numbers.insert(command_list[2], command_list[1])
    elif "Remove" in command:
        command_list = command.split()
        command_list[1] = int(command_list[1])
        if command_list[1] > len(list_numbers):
            print(f"Invalid index")
        else:
            list_numbers.remove(list_numbers[command_list[1]])
    elif "Shift left" in command:
        command_list = command.split()
        command_list[2] = int(command_list[2])
        for _ in range(command_list[2]):
            list_numbers.append(list_numbers.pop(0))
    elif "Shift right" in command:
        command_list = command.split()
        command_list[2] = int(command_list[2])
        for _ in range(command_list[2]):
            list_numbers[len(list_numbers) - 1], list_numbers[0] = list_numbers[0], list_numbers[len(list_numbers) - 1]
    command = input()
for i in range(len(list_numbers)):
    list_numbers[i] = int(list_numbers[i])

list_numbers_str = "".join(str(list_numbers))
print(list_numbers_str)
