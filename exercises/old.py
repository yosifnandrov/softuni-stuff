events = input().split("|")

energy = 100
coins = 100
all_events = True

for event_info in events:
    event, number = event_info.split("-")
    number = int(number)
    if event == "rest":
        if energy + number > 100:
            gained = 100 - energy
            energy += gained
            print(f"You gained {gained} energy.")
        else:
            energy += number
            print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy - 30 >= 0:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins - number >= 0:
            coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            all_events = False
            break
if all_events:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")