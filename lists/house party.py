number_commands = int(input())
party_list = []
for _ in range(number_commands):
    command = input()
    if "not" in command:
        command_list = command.split()
        if command_list[0] in party_list:
            party_list.remove(command_list[0])
        else:
            print(f"{command_list[0]} is not in the list!")
    else:
        command_list = command.split()
        if command_list[0] in party_list:
            print(f"{command_list[0]} is already in the list!")
        else:
            party_list.append(command_list[0])
for name in party_list:
    print(name)
