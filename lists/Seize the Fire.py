fire_data = input().split("#")
water = int(input())
HIGH_RANGE = range(81, 126)
MEDIUM_RANGE = range(51, 81)
LOW_RANGE = range(1, 51)
effort = 0
total_fire = 0
print("Cells:")
for cell in fire_data:
    type_fire, value = cell.split(" = ")
    value = int(value)
    if type_fire == "High" and value not in HIGH_RANGE:
        continue
    elif type_fire == "Medium" and value not in MEDIUM_RANGE:
        continue
    elif type_fire == "Low" and value not in LOW_RANGE:
        continue
    if water >= value:
        water -= value
        effort += value * 0.25
        total_fire += value
        print(f" - {value}")

    else:
        continue

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")


