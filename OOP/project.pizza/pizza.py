from typing import Dict
from collections import defaultdict


class Pizza:
    name: str
    dough: "Dough"
    toppings: Dict[str,float]
    toppings_capacity: int

    def __init__(self,name:str,dough:"Dough",toppings_capacity:int):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = defaultdict(float)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name = new_name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self,new_dough):
        self.__dough = new_dough

    @property
    def topping_capacity(self):
        return self.__toppings_capacity

    @topping_capacity.setter
    def topping_capacity(self,new_capacity):
        self.__toppings_capacity = new_capacity

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self,new_toppings):
        self.__toppings = new_toppings

    def add_topping(self,topping:"Topping"):
        if len(self.__toppings) < self.__toppings_capacity:
            self.__toppings[topping.topping_type] += topping.weight
        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        dough = self.__dough.weight
        topping_weight = 0
        for topping, weight in self.__toppings.items():
            topping_weight += weight
        return dough + topping_weight




