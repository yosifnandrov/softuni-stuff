def multiply(times):
    def decorator(fn):
        def wrapper(*args,**kwargs):
            res = fn(*args,**kwargs)
            return res * times
        return wrapper
    return decorator


@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))