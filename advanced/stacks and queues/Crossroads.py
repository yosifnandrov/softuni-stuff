from collections import deque

green_light = int(input())
free_window = int(input())
command = input()
cars = deque()
cars_crossed = 0
new_green_light = green_light
while not command == "END":
    green_light = new_green_light
    if not command == "green":
        cars.append(command)
    else:
        while cars:
            crossing_car = cars.popleft()
            if len(crossing_car) > green_light:
                value = len(crossing_car) - green_light
                if free_window - value < 0:
                    print(f"A crash happened!")
                    print(f"{crossing_car} was hit at {crossing_car[free_window - value]}.")
                    exit()
                else:
                    cars_crossed += 1
                    break
            else:
                cars_crossed += 1
                green_light -= len(crossing_car)
    command = input()

print(f"Everyone is safe.")
print(f"{cars_crossed} total cars passed the crossroads.")