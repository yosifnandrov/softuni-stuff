class reverse_iter:
    def __init__(self,iterable):
        self.iterable = iterable
        self.index = len(self.iterable) - 1


    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        else:
            self.index = self.index - 1
            return self.iterable[self.index + 1]

reversed_list = reverse_iter([10,1,15,22,75,12])
for item in reversed_list:
    print(item)
