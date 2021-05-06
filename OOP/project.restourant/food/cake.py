from project_animals.food.dessert import Dessert


class Cake(Dessert):

    def __init__(self, name, price=5, grams=250,calories = 1000):
        super().__init__(name, price, grams)
        self.calories = calories
        Cake.CALORIES = self.calories
        Cake.PRICE = self.price
        Cake.GRAMS = self.grams
