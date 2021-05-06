people = int(input())
days = int(input())
money = 0
for i in range(1, days + 1):
    is_motivational = False
    if i % 10 == 0:
        people -= 2
    if i % 15 == 0:
        people += 5
    money += 50
    money -= 2 * people
    if i % 3 == 0:
        money -= 3 * people
        is_motivational = True
    if i % 5 == 0:
        money += 20 * people
        if is_motivational:
            money -= 2 * people

print(f"{people} companions received {int(money / people)} coins each.")


