from project_animals.motorcycle import MotorCycle
from project_animals.family_car import FamilyCar
from project_animals.vehicle import Vehicle
from project_animals.cross_motorcycle import CrossMotorcycle
from project_animals.car import Car
from project_animals.race_motorcycle import RaceMotorcycle
from project_animals.sport_car import SportCar


klasses = [Vehicle,MotorCycle,Car,CrossMotorcycle,RaceMotorcycle,FamilyCar,SportCar]

for klas in klasses:
    print(klas.__name__, klas.__mro__[1].__name__)