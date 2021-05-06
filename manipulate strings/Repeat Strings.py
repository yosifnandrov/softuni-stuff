strings = input().split()

for index in range(len(strings)):
    result = strings[index]*len(strings[index])
    print(result,end="")
