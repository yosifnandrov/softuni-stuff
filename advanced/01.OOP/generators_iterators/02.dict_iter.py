from typing import Dict, Any


class dictionary_iter:

    def __init__(self,dict:Dict[Any,Any]):
        self.dict = dict
        self.__dict = iter(self.dict.items())

    def __iter__(self):
        self.__dict = iter(self.dict.items())
        return self

    def __next__(self):
        value = next(self.__dict)
        return value

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


print(result.dict)
