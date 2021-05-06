n = int(input())
invited = set()
for _ in range(n):
    guest = input()
    invited.add(guest)

came = input()

while not came == "END":
    if came in invited:
        invited.remove(came)
    came = input()

print(len(invited))

for guests in sorted(invited):
    print(guests)