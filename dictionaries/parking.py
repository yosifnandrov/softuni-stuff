number_commands = int(input())
register_dict = {}
for cmd in range(number_commands):
    counter = 0
    data = input().split()
    for word in data:
        counter += 1
    if counter == 3:
        command, username, licenseplate = data[0],data[1],data[2]
    else:
        command,username = data[0],data[1]
    if command == "register":
        if username in register_dict:
            print(f"ERROR: already registered with plate number {register_dict[username]}")
        else:
            register_dict[username] = licenseplate
            print(f"{username} registered {register_dict[username]} successfully")
    elif command == "unregister":
        if username not in register_dict:
            print(f"ERROR: user {username} not found")
        else:
            register_dict.pop(username)
            print(f"{username} unregistered successfully")

for user, license in register_dict.items():
    print(f"{user} => {license}")

