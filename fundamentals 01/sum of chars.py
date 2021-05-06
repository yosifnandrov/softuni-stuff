n = int(input())
sum_ascii = 0
for s in range(1, n + 1):
    symbol = input()
    sum_ascii += ord(symbol)
print(f"The sum equals: {sum_ascii}")