def numbers():
    i = 1
    while True:
        yield i
        i += 1


def take(count_to_take,sequence):
    return [x for _,x in zip(range(count_to_take),sequence)]


def halves():
    for x in numbers():
        yield x/2


def solution():
    return take,halves,numbers

print(take(3,"kosmonaft"))