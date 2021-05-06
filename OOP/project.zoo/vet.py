from project_animals.animal_init import initialization_animals


class Vet:
    name: str
    age: int
    salary: int

    __init__ = initialization_animals

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"