password = input()
command = input()

while not command == "Done":
    if command == "TakeOdd":
        password = [password[i] for i in range(len(password)) if i % 2 == 1]
        password = "".join(password)
        print(password)
    elif "Cut" in command:
        cmd,index,lenght = command.split()
        index = int(index)
        lenght = int(lenght)
        password = password.replace(password[index:index+lenght], "", 1)
        print(password)
    elif "Substitute" in command:
        cmd,substring,substitute = command.split()
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")