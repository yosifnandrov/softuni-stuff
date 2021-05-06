N = int(input())

matrix = [
    list(str(input().strip()))
    for _ in range(N)
]


movements = {
    "LEFT,UP": (-1,-2),
    "RIGHT,UP":(-1,2),
    "UP,LEFT":(-2,-1),
    "UP,RIGHT":(-2,1),
    "LEFT,DOWN":(1,-2),
    "RIGHT,DOWN":(1,2),
    "DOWN,LEFT":(2,-1),
    "DOWN,RIGHT":(2,1)
}



def find_collisions(matrix, tuple):
    i, j = tuple
    collisions = {(i,j):0}
    for movement in movements:
        k,l = movements[movement]
        if 0 <= i+k <= N-1 and 0 <= j+l <= (len(matrix[i])-1):
            if matrix[i+k][j+l] == "K":
                collisions[i,j] += 1
    if collisions[(i,j)]>0:
        return collisions
    return


counter = 0

while True:
    crashes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "K":
                if find_collisions(matrix,(i,j)):
                    crashes.append(find_collisions(matrix,(i,j)))
    if not crashes:
        break
    number_of_crashes = []
    for crash in crashes:
        for value in crash.values():
            number_of_crashes.append(value)

    number_of_crashes = sorted(number_of_crashes)

    for crash in crashes:
        for coords, num in crash.items():
            if num == number_of_crashes[-1]:
                i, j = coords
                matrix[i][j] = "0"
                counter += 1
                crashes.clear()



print(counter)