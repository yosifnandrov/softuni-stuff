deck = input().split()
shuffles = int(input())

top_card = deck[0]
bottom_card = deck[-1]
half = len(deck) // 2
for shuffle in range(shuffles):
    left_deck = []
    right_deck = []
    shuffled_deck = []

    for index in range(1, half):
        left_deck.append(deck[index])

    for index in range(half, len(deck) - 1):
        right_deck.append(deck[index])

    for index in range(len(right_deck)):
        shuffled_deck.append(right_deck[index])
        shuffled_deck.append(left_deck[index])
    deck = shuffled_deck.copy()
    deck.append(bottom_card)
    deck.insert(0, top_card)

print(deck)


