def even_parameters(fn):
    def wrapper(*args,**kwargs):
        if all(even(num) for num in args):
            return fn(*args,**kwargs)
        return "Please use only even numbers!"
    return wrapper


def even(number):
    try:
        if number % 2 == 0:
            return True
    except TypeError:
        return False


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))