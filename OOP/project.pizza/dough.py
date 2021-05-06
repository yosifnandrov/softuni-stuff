class Dough:
    flour_type: str
    baking_technique: str
    weight: float

    def __init__(self,flour_type:str,baking_technique:str,weight:float):
        self.__flour_type = flour_type
        self.__baking_technique = baking_technique
        self.__weight = weight

    @property
    def flour_type(self):
        return self.__flour_type

    @flour_type.setter
    def flour_type(self,new_type):
        self.__flour_type = new_type

    @property
    def baking_technique(self):
        return self.__baking_technique

    @baking_technique.setter
    def baking_technique(self,new_technique):
        self.__baking_technique = new_technique

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self,new_weight):
        self.__weight = new_weight


