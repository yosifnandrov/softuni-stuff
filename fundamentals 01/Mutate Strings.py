first_string = input()
second_string = input()
result = ""
previous_string = first_string
for index in range(len(first_string)):
    for i in range(index + 1):
        result += second_string[i]
    for i in range(index + 1, len(second_string)):
        result += first_string[i]
    if not result == previous_string:
        print(result)
    previous_string = result
    result = ""