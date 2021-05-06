import sys
n = int(input())
max_value = -sys.maxsize
snow = 0
time = 0
quality = 0
for i in range(1, n + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > max_value:
        snow = snowball_snow
        time = snowball_time
        quality = snowball_quality
        max_value = snowball_value
print(f"{snow} : {time} = {int(max_value)} ({quality})")

