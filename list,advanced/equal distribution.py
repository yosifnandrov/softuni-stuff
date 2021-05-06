numbers = input().split(", ")
minimum = int(input())
def sum_list(some_list):
    sum_n = 0
    for n in some_list:
        n = int(n)
        sum_n += n
    return sum_n
def max_num(some_list):
    for n in range(len(some_list)):
        a =5
    return max(some_list)

for n in range(len(numbers)):
    if sum_list(numbers) // len(numbers) < minimum:
        print("No equal distribution possible")
    numbers[n] = int(numbers[n])
    diff = numbers[n] - minimum
    if diff < 0:
        numbers[n] += abs(diff)
        max_num(numbers) -= abs(diff)
print(numbers)





