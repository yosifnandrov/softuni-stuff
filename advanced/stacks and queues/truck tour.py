from collections import deque

petrol_pumps = int(input())
petrols = deque()
temp_queue = deque()
for i in range(petrol_pumps):
    pump_info = list(map(int, input().split()))
    petrols.append(pump_info[0] - pump_info[1])



for i in range(petrol_pumps):
    is_valid = True
    total_fuel = 0
    while petrols:
        pump = petrols.popleft()
        total_fuel += pump
        if total_fuel < 0:
            is_valid = False
            petrols.append(pump)
            break
    if is_valid:
        print(i)
        break





