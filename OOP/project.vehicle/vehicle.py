class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float
    fuel_consumption: float
    fuel: float
    horse_power: int

    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self,fuel:float,horse_power:int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self,kms:int):
        if kms * self.fuel_consumption > self.fuel:
            return
        self.fuel -= kms * self.fuel_consumption
        return



# vehicle = Vehicle(50, 150)
# print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
# print(vehicle.fuel)
# print(vehicle.horse_power)
# print(vehicle.fuel_consumption)
# vehicle.drive(100)
# print(vehicle.fuel)

