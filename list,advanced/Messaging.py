number = input().split()
message = input()

def get_sum(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum

for i in number:
    summary = get_sum(i)
    for l in range(len(message)):
        if l == summary:
            print(message[l], end="")
            message = message[0:l:] + message[l + 1::]
            break
        elif l == len(message) - 1:
            l = summary - len(message)
            print(message[l], end="")
            message = message[0:l:] + message[l + 1::]





