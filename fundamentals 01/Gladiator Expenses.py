lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
repair_cost = 0
counter = 0
for l in range(1, lost_fights + 1):
    no_helmet = False
    no_sword = False
    if l % 2 == 0:
        repair_cost += helmet_price
        no_helmet = True
    if l % 3 == 0:
        repair_cost += sword_price
        no_sword = True
    if no_helmet and no_sword:
        repair_cost += shield_price
        counter += 1
        if counter == 2:
            repair_cost += armor_price
            counter = 0
print(f"Gladiator expenses: {repair_cost:.2f} aureus")