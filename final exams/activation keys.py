raw_text = input()

command = input()

while not command == "Generate":
    command = command.split(">>>")
    if len(command) == 2:
        substring = command[1]
        if substring in raw_text:
            print(f"{raw_text} contains {substring}")
        else:
            print("Substring not found!")
    elif len(command) == 4:
        start_ind = int(command[2])
        end_ind = int(command[3])
        if raw_text[start_ind:end_ind].islower():
            raw_text = raw_text.replace(raw_text[start_ind:end_ind], raw_text[start_ind:end_ind].upper())
        else:
            raw_text = raw_text.replace(raw_text[start_ind:end_ind], raw_text[start_ind:end_ind].lower())
        print(raw_text)
    elif len(command) == 3:
        start_ind = int(command[1])
        end_ind = int(command[2])
        raw_text = raw_text.replace(raw_text[start_ind:end_ind], "")
        print(raw_text)

    command = input()

print(f"Your activation key is: {raw_text}")
