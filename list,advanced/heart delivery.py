hood = input().split("@")
hood = [int(i) for i in hood]
jumps = input()
current_index = 0
counter = 0
while not jumps == "Love!":
    action, index = jumps.split()
    index = int(index)
    current_index += index
    if current_index > len(hood) - 1:
        current_index = 0
        if hood[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
            jumps = input()
            continue
        else:
            hood[0] -= 2
    else:
        if hood[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
            jumps = input()
            continue
        else:
            hood[current_index] -= 2
    if hood[current_index] == 0:
        print(f"Place {current_index} has Valentine's day.")
    jumps = input()
print(f"Cupid's last position was {current_index}.")
for n in range(len(hood)):
    if hood[n] > 0:
        counter += 1
if counter > 0:
    print(f"Cupid has failed {counter} places.")
if counter == 0:
    print("Mission was successful.")

