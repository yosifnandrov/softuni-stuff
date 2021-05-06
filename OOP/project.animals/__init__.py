
from project.animals import *
from project.animals.birds import Owl, Hen
from project.food import Meat, Vegetable, Fruit, Seed
from project.animals.mammals import Tiger, Cat, Dog, Mouse

mice = Mouse("jerry",10,"bulgaria")
print(mice.weight)
print(mice.food_eaten)
vegie = Vegetable(3)
fruit = Fruit(2)
meat = Meat(1)
seed = Seed(2)

print(mice.feed(meat))
print(mice.feed(seed))
print(mice.feed(fruit))
print(mice.feed(vegie))
print(mice.food_eaten)
print(mice.name)
print(mice.living_region)