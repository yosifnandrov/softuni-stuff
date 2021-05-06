from abc import ABC


class Food(ABC):

    def __init__(self,quantity:int):
        self.quantity = quantity


class Vegetable(Food):
    pass


class Meat(Food):
    pass


class Seed(Food):
    pass


class Fruit(Food):
    pass


def get_subclasses_food():
    subclasses = []
    for name in Food.__subclasses__():
        subclasses.append(name.__name__)
    return subclasses

