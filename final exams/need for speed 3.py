number_of_cars = int(input())
cars_dict = {}
for i in range(number_of_cars):
    cars = input()
    model,miles,fuel = cars.split("|")
    miles = int(miles)
    fuel = int(fuel)
    cars_dict[model] = [miles,fuel]

command = input()

while not command == "Stop":
    if "Drive" in command:
        cmd,model,dist,fuel = command.split(" : ")
        dist = int(dist)
        fuel = int(fuel)
        if cars_dict[model][1] < fuel:
            print(f"Not enough fuel to make that ride")
        else:
            cars_dict[model][1] -= fuel
            cars_dict[model][0] += dist
            print(f"{model} driven for {dist} kilometers. {fuel} liters of fuel consumed.")
        if cars_dict[model][0] >= 100000:
            cars_dict.pop(model)
            print(f"Time to sell the {model}!")
    elif "Refuel" in command:
        cmd,model,fuel = command.split(" : ")
        fuel = int(fuel)
        if cars_dict[model][1] + fuel > 75:
            filled = 75 - cars_dict[model][1]
            cars_dict[model][1] = 75
            print(f"{model} refueled with {filled} liters")
        else:
            cars_dict[model][1] += fuel
            print(f"{model} refueled with {fuel} liters")
    elif "Revert" in command:
        cmd, model, dist = command.split(" : ")
        dist = int(dist)
        if cars_dict[model][0] - dist < 10000:
            cars_dict[model][0] = 10000
        else:
            cars_dict[model][0] -= dist
            print(f"{model} mileage decreased by {dist} kilometers")
    command = input()

cars_dict = dict(sorted(cars_dict.items(), key = lambda x:x[0]))
cars_dict = dict(sorted(cars_dict.items(),key = lambda x:x[1][0],reverse=True))

for car, miles_fuel in cars_dict.items():
    print(f"{car} -> Mileage: {miles_fuel[0]} kms, Fuel in the tank: {miles_fuel[1]} lt.")

