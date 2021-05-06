capacity = 255
sum_liters = 0
n = int(input())
for i in range(n):
    liters = int(input())
    sum_liters += liters
    if sum_liters > capacity:
        sum_liters -= liters
        print(f"Insufficient capacity!")
print(f"{sum_liters}")

