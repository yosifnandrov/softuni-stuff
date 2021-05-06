elements = input().split()
guesses = input()
moves = 0
while not guesses == "end":
    guesses = guesses.split()
    in_range = True
    guesses = [int(i) for i in guesses]
    moves += 1
    for i in range(len(guesses)):
        if guesses[i] not in range(len(elements)) or guesses[0] == guesses[1]:
            in_range = False
    if not in_range:
        for num in range(len(guesses)):
            elements.insert(len(elements) // 2, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif elements[guesses[0]] == elements[guesses[1]]:
        new_list = elements.copy()
        to_be_removed = elements[guesses[0]]
        for ind in range(len(guesses)):
            elements.remove(to_be_removed)
        print(f"Congrats! You have found matching elements - {new_list[guesses[0]]}!")
    else:
        print(f"Try again!")
    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break
    new_list = elements.copy()
    guesses = input()

if len(elements) > 0:
    elements_str = " ".join(elements)
    print(f"Sorry you lose :(\n{elements_str}")






