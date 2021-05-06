from project_animals.animal_init import initialization_animals


class Lion:
    name: str
    gender: str
    age: int

    __init__ = initialization_animals

    @staticmethod
    def get_needs():
        return 50

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


