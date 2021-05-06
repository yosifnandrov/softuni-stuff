budget = float(input())
flour_kg = float(input())
eggs = .75 * flour_kg
milk = flour_kg
milk += (flour_kg * 0.25)
milk = milk / 4
one = milk + eggs + flour_kg
colored_eggs = 0
counter = 0
counter_two = 0

while budget > 0:
    budget -= one
    if budget < 0:
        budget += one
        break
    counter_two += 1
    colored_eggs += 3
    counter += 1
    if counter_two == 3:
        colored_eggs -= counter - 2
        counter_two = 0
print(f"You made {counter} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
