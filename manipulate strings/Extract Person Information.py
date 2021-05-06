times = int(input())

start_name = None
end_name = None
start_age = None
end_age = None

for n in range(times):
    sentance = input()
    for i in range(len(sentance)):
        char = sentance[i]
        if char == "@":
            start_name = i + 1
        elif char == "|":
            end_name = i
        elif char == "#":
            start_age = i + 1
        elif char == "*":
            end_age = i
    print(f"{sentance[start_name:end_name]} is {sentance[start_age:end_age]} years old.")


