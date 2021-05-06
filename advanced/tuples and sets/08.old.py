import sys
numbers = []
n = int(input())
max_diff = -sys.maxsize
for _ in range(n):
    num_one = int(input())
    num_two = int(input())
    sum_nums = num_one + num_two
    if not numbers:
        numbers.append(sum_nums)
    else:
        if sum_nums not in numbers:
            last_number = numbers[-1]
            if max_diff < abs(sum_nums - last_number):
                max_diff = abs(sum_nums - last_number)
            numbers.append(sum_nums)
if max_diff == -sys.maxsize:
    print(f"Yes, value={numbers[0]}")
else:
    print(f"No, maxdiff={max_diff}")

