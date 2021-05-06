numbers = input()
numbers_list = numbers.split()
command = input()
is_same = True
while not command == "end":
    if "Delete" in command:
        command_list = command.split("Delete ")
        command_str = "".join(command_list)
        while command_str in numbers_list:
            for n in numbers_list:
                if n == command_str:
                    numbers_list.remove(n)
        command = input()
    elif "Insert" in command:
        command_list_insert = command.split("Insert ")
        command_list_insert_str = "".join(command_list_insert)
        command_list_insert_list = command_list_insert_str.split()
        first_number = (command_list_insert_list[0])
        second_number = int(command_list_insert_list[1])
        numbers_list.insert(second_number, first_number)
        command = input()
numbers_list_str = " ".join(numbers_list)

print(numbers_list_str)
