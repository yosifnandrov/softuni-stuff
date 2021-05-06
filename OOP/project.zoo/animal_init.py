def initialization_animals(self,*args):
    attributes = self.__annotations__
    for attr,argument in zip(attributes,args):
        setattr(self,attr,argument)



