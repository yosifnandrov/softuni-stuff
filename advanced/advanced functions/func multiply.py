# def multiply(*args):
#     multiplyer = 1
#     args = [str(el) for el in args]
#     for i in range(len(args)):
#         multiplyer = int(args[i])*multiplyer
#     return multiplyer
#

# print(multiply(2, 0, 1000, 5000))

from functools import reduce

multiply = lambda *args:reduce(lambda a,b: a*b, args)

print(multiply(2, 7, 1001, 5020))