def abs_values(*args):
    for nums in args:
        b = [num*(-1) if num < 0 else num for num in nums]
        return b


my_args = [float(el) for el in input().split()]

print(abs_values(my_args))




