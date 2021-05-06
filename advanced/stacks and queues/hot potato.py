from collections import deque

people = deque(input().split(" "))
toss = int(input())

while len(people)>1:
    people.rotate(-toss)
    loser = people.pop()
    print(f"Removed {loser}")

winner = people.pop()
print(f"Last is {winner}")

