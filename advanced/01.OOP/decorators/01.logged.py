def logged(fn):
    def wrapper(*args,**kwargs):
        first_line = f"you called {fn.__name__}{args}"
        second_line = f"it returned {fn(*args)}"
        return first_line + '\n' + second_line
    return wrapper

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))

