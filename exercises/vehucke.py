class Vehicle:

    def __init__(self,type,model,price,owner = None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner


    def buy(self,money,new_owner):
        self.money = money
        self.new_owner = new_owner
        change = self.money - self.price
        if self.money >= self.price and self.owner is None:
            self.owner = self.new_owner
            return f"Successfully bought a {self.type}. Change: {change:.2f}"
        elif self.money < self.price:
            return "Sorry, not enough money"
        elif self.owner is not None:
            return "Car already sold"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)


