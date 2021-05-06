from collections import defaultdict
information = input()
phone_book = defaultdict(str)
while not information.isdigit():
    name, phone_number = information.split("-")
    phone_book[name] = phone_number
    information = input()

if information.isdigit():
    for _ in range(int(information)):
        searched = input()
        if searched in phone_book:
            print(f"{searched} -> {phone_book[searched]}")
        else:
            print(f"Contact {searched} does not exist.")



