from itertools import permutations

board = [
    input().split()
    for _ in range(8)
]


movements = list(permutations(range(-1,2),2))
movements.append((1,1))
movements.append((-1,-1))

queens = []

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == "K":
            for k,l in movements:
                m,n = k,l
                while 0 <= i + m < len(board) and 0 <= j + n < len(board):
                    if board[i+m][j+n] == "Q":
                        queens.append((i+m,j+n))
                        break
                    m, n = m + k, n + l


if queens:
    for queen in queens:
        print(list(queen))
else:
    print("The king is safe!")



