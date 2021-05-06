concealed_msg = input()

command = input()

while not command == "Reveal":
    command = command.split(":|:")
    if len(command) == 2:
        if "InsertSpace" in command:
            cmd, index = command
            index = int(index)
            concealed_msg = concealed_msg[:index] + " " + concealed_msg[index:]
            print(concealed_msg)
        elif "Reverse" in command:
            cmd,substring = command
            if substring in concealed_msg:
                concealed_msg = concealed_msg.replace(substring, "", 1)
                concealed_msg = concealed_msg + substring[::-1]
                print(concealed_msg)
            else:
                print("error")
    else:
        cmd,substring,replacement = command
        concealed_msg = concealed_msg.replace(substring,replacement)
        print(concealed_msg)
    command = input()

print(f"You have a new text message: {concealed_msg}")