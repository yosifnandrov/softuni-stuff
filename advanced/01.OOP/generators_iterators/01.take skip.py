class take_skip:
    def __init__(self,step:int,count:int):
        self.step = step
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += self.step
        if self.index - self.step == self.count * self.step:
            raise StopIteration
        else:
            return self.index - self.step



numbers = take_skip(10, 5)
for number in numbers:
    print(number)