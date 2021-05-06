first_line = input()
second_line = input()

while first_line in second_line:
    for i in range(len(second_line)):
        if second_line[i:i+len(first_line)] == first_line:
            second_line = second_line[:i:] + second_line[i+len(first_line)::]

print(second_line)