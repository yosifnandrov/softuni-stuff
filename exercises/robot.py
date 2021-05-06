class Robocop:

    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def introduce_self(self):
        return f"Hello my name is {self.name}"
    def __repr__(self):
        return f"{self.name},{self.color},{self.weight}"
r1 = Robocop("Tom","red", 30)
print(r1.introduce_self())
r2 = Robocop("Jerry", "blue", 40)
print(r2)
class Person:
    def __init__(self, name, personality, isSitting, robotOwned):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
        self.robotOwned = robotOwned

    def sit_down(self):
        self.isSitting = True
        return f"{self.name} is sitting"

    def stand_up(self):
        self.isSitting = False
        return f"{self.name} is standing"
    def __repr__(self):
        return f"{self.name} is {self.personality} and owns {self.robotOwned}"
p1 = Person("Alice", "aggresive", False, "r2")
p2 = Person("Becky", "talkative", True, "r1")
print(p1.sit_down())
print(p2.stand_up())
print(p2)
print(p1)