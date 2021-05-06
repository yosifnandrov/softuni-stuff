from project.animals.animal import Mammal
from project.food import Food


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self,food:Food):
        if not food.__class__.__name__ == "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.40 * food.quantity
        self.food_eaten += food.quantity


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self,food:Food):
        if food.__class__.__name__ not in ["Vegetable","Fruit"]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.10 * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self,food:Food):
        if food.__class__.__name__ not in ["Vegetable", "Meat"]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.30 * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self,food:Food):
        if not food.__class__.__name__ == "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 1.00 * food.quantity
        self.food_eaten += food.quantity
