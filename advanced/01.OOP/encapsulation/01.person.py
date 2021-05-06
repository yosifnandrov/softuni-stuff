class Person:

    def __init__(self,name:str,age:int):
        self.__age = age
        self.__name = name

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name


person = Person("yosif", 28)

print(person.get_name())