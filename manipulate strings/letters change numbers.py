from decimal import Decimal
import string

task = input().split()

def give_me_alphabet_position(a):
    a = a.lower()
    position = string.ascii_lowercase.index(a) + 1
    return position

total_sum = 0
for element in task:
    number = int(element[1:-1])
    front_position = give_me_alphabet_position(element[0])
    back_position = give_me_alphabet_position(element[-1])
    if element[0].isupper():
        result = number / front_position
    else:
        result = number * front_position
    if element[-1].isupper():
        result -= back_position
    else:
        result += back_position
    total_sum += result

print(f"{round(Decimal(total_sum),2)}")