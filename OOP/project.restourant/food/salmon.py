from project_animals.food.main_dish import MainDish


class Salmon(MainDish):

    def __init__(self,name,price,grams = 22):
        super().__init__(name,price,grams)
        Salmon.GRAMS = self.grams
