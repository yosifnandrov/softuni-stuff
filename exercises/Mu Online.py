health = 100
bitcoins = 0
have_died = False
dungeon_rooms = input().split("|")
counter = 0

for room in dungeon_rooms:
    counter += 1
    action,value = room.split(" ")
    value = int(value)
    if action == "potion":
        if health + value > 100:
            diff = health + value - 100
            value -= diff
            health += value
        else:
            health += value
        print(f"You healed for {value} hp.")
        print(f"Current health: {health} hp.")
    elif action == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        if health - value > 0:
            health -= value
            print(f"You slayed {action}.")
        else:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {counter}")
            have_died = True
            break
if not have_died:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")

