from random import choice


class RandomList(list):

    def get_random_element(self):
        element = choice(self)
        self.pop(self.index(element))
        return element


rl = RandomList([1,2,3,4,5,56,6,7,88,32,5])
print(rl.get_random_element())
print(rl)