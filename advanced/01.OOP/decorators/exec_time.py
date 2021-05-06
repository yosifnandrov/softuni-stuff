import time


def exec_time(fn):
    def wrapper(*args,**kwargs):
        start = time.time()
        fn(*args)
        end = time.time()
        return end - start
    return wrapper

@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 100000))
