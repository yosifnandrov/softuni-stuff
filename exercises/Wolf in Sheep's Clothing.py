text = input().split(", ")
text = list(reversed(text))
for i in range(len(text)-1,-1,-1):
    if text[0] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    else:
        if text[i] == "wolf":
            print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")
            break
