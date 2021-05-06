class sequence_repeat:

    def __init__(self,sequence:str,times:int):
        self.sequence = sequence
        self.times = times
        self.index = 0



    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.times:
            raise StopIteration
        else:
            self.index += 1
            return self.sequence[(self.index - 1) % len(self.sequence)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')