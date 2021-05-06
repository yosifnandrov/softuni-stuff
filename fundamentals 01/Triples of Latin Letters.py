n = int(input())

for i in range(n):
    for b in range(n):
        for c in range(n):
             print(f"{chr(97 + i)}{chr(97 + b)}{chr(97 + c)}")