first_char = input()
second_char = input()

line_of_text = input()
total_sum = 0
for char in line_of_text:
    for i in range(ord(first_char) + 1, ord(second_char)):
        if char == chr(i):
            total_sum += i
            break

print(total_sum)


