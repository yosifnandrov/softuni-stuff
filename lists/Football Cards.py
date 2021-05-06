cards = input()
A = 11
B = 11
list_cards = cards.split()
list_cards = set(list_cards)
for n in list_cards:
    if "A" in n:
        A -= 1
    elif "B" in n:
        B -= 1
print(f"Team A - {A}; Team B - {B}")
if A < 7 or B < 7:
    print(f"Game was terminated")