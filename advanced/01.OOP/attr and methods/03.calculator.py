import operator
from functools import reduce


class Calculator:

    @staticmethod
    def add(*args):
        return reduce(operator.add, args)

    @staticmethod
    def divide(*args):
        return reduce(operator.truediv, args)

    @staticmethod
    def subtract(*args):
        return reduce(operator.sub, args)

    @staticmethod
    def multiply(*args):
        return reduce(operator.mul, args)


