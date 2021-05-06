gifts = input().split()
command = input()

while not command == "No Money":
    if "OutOfStock" in command:
        com, value = command.split()
        gifts = [None if x == value else x for x in gifts]
        command = input()
    elif "Required" in command:
        com, value, index = command.split()
        index = int(index)
        if index > len(gifts) - 1:
            command = input()
            continue
        gifts[index] = value
        command = input()
    elif "JustInCase" in command:
        com, value = command.split()
        gifts[-1] = value
        command = input()
gifts = [x for x in gifts if x is not None]
gift_as_str = " ".join(gifts)
print(gift_as_str)

