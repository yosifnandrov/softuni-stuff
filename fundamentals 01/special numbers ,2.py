n = int(input())

for num in range(1, n + 1):
    num_to_str = str(num)
    sum_digits = 0
    for i in num_to_str:
        sum_digits += int(i)
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")