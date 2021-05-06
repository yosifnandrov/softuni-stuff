class Mammal:
    name:str
    type:str
    sound:str
    __kingdom = "animals"

    def __init__(self,name:str,type:str,sound:str):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    @classmethod
    def get_kingdom(cls):
        return cls.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"

