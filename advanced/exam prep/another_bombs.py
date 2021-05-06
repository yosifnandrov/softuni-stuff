from collections import deque

bomb_effects = deque([int(el) for el in input().split(", ")])
bomb_castings = [int(el) for el in input().split(", ")]

DATURA_BOMBS = 40
CHERRY_BOMBS = 60
SMOKE_DECOY_BOMBS = 120

my_bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}
bomb_pouch = False
while bomb_castings:
    if not bomb_effects:
        break
    bomb_cast = bomb_castings.pop()
    bomb_effect = bomb_effects.popleft()
    while bomb_cast >= 0:
        if bomb_cast + bomb_effect == DATURA_BOMBS:
            my_bombs["Datura Bombs"] += 1
            bomb_cast = 0
        elif bomb_cast + bomb_effect == CHERRY_BOMBS:
            my_bombs["Cherry Bombs"] += 1
            bomb_cast = 0
        elif bomb_cast + bomb_effect == SMOKE_DECOY_BOMBS:
            my_bombs["Smoke Decoy Bombs"] += 1
            bomb_cast = 0
        bomb_cast -= 5
    if all(v >= 3 for v in my_bombs.values()):
        bomb_pouch = True
        break

if bomb_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print("Bomb Effects: empty")

if bomb_castings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_castings))}")
else:
    print("Bomb Casings: empty")

for k,v in sorted(my_bombs.items()):
    print(f"{k}: {v}")