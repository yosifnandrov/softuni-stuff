class Human:

    def __init__(self,name:str,age:int,gender:str):
        self.__name = name
        self.__age = age
        self.__gender = gender


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    def __repr__(self):
        return f"{self.__name} is {self.__age} years old {self.__gender}"

h = Human("gosho",20,"male")
print(h.__repr__())
h.name = "pesho"
print(h.__repr__())