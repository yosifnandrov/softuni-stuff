def round_that(*args):
    for nums in args:
        b = [round(num) for num in nums]
        return b


request = [float(el) for el in input().split()]

print(round_that(request))
