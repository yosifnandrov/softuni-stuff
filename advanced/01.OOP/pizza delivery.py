class PizzaDelivery:

    def __init__(self,name: str, price:float,ingredients:dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self,ingredient:str,quantity:int,ingredient_price:float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity
        self.price += ingredient_price*quantity

    def remove_ingredient(self,ingredient:str,quantity:int,ingredient_price:float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        else:
            if self.ingredients[ingredient] < quantity:
                return f"Please check again the desired quantity of {ingredient}!"
            else:
                self.ingredients[ingredient] -= quantity
                self.price -= ingredient_price*quantity

    def make_order(self):
        all_ingredients = ", ".join(f"{k}: {v}" for k,v in self.ingredients.items())
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {all_ingredients} and the price will be {self.price}lv."



