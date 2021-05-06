quantity = int(input())
days = int(input())
ornament = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
christmas_spirit = 0
money = 0

for i in range(1, days + 1):
    have_bought = False

    if i % 11 == 0:
        quantity += 2

    if i % 2 == 0:
        money += quantity * ornament
        christmas_spirit += 5

    if i % 3 == 0:
        money += (tree_skirt + tree_garlands) * quantity
        christmas_spirit += 13
        have_bought = True

    if i % 5 == 0:
        money += tree_lights * quantity
        christmas_spirit += 17
        if have_bought:
            christmas_spirit += 30

    if i % 10 == 0:
        christmas_spirit -= 20
        money += tree_skirt + tree_garlands + tree_lights

    if i == days and i % 10 == 0:
        christmas_spirit -= 30

print(f"Total cost: {money}")
print(f"Total spirit: {christmas_spirit}")



