def type_check(some_type):
    def decorator(fn):
        def wrapper(*args,**kwargs):
            if all(isinstance(arg, some_type) for arg in args):
                return fn(*args)
            return "Bad Type"
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))