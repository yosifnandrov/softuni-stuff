rooms = int(input())
enough_chairs = True
free_chairs = 0
for i in range(1, rooms + 1):
    chairs_in_the_room = input()
    chair, taken = chairs_in_the_room.split()
    taken = int(taken)
    if len(chair) < taken:
        print(f"{abs(len(chair) - taken)} more chairs needed in room {i}")
        enough_chairs = False
    else:
        free_chairs += abs(taken - len(chair))
if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")


