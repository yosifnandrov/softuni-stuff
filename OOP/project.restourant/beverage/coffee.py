from project_animals.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):

    def __init__(self, name, caffeine, price=3.50,milliliters = 50):
        super().__init__(name, price)
        self.milliliters = milliliters
        self.caffeine = caffeine
        Coffee.PRICE = self.price
        Coffee.MILLILITERS = self.milliliters

