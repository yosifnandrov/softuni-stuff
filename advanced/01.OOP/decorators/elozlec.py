def debug_add(fn):
    def wrapper(*args,**kwargs):
        for i in range(len(args)):
            print(args[i])
        return fn(*args)
    return wrapper


@debug_add
def add(a,b):
    return a + b


print(add(2,3))