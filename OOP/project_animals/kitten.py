class Kitten(Cat):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.gender = "Female"

    def make_sound(self):
        return "Meow"

kiten = Kitten("mqul",10)
print(kiten.gender)
print(kiten.make_sound())