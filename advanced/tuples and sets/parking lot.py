n = int(input())
in_parking_lot = set()
for _ in range(n):
    direction, car = input().split(", ")
    if direction == "IN":
        in_parking_lot.add(car)
    elif direction == "OUT":
        if car in in_parking_lot:
            in_parking_lot.remove(car)
if in_parking_lot:
    for reg_num in in_parking_lot:
        print(reg_num)
else:
    print("Parking lot is Empty")
