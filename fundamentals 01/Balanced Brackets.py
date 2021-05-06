n = int(input())
counter = 0
counter_two = 0
for i in range(1, n + 1):
    symbol = input()
    if symbol == "(":
        counter += 1
    elif symbol == ")":
        counter_two += 1
if counter == 0 and counter_two == 0:
    print("BALANCED")
elif counter % 2 == 0 and counter_two == 0:
    print("BALANCED")
elif counter == counter_two:
    print("BALANCED")
else:
    print("UNBALANCED")

