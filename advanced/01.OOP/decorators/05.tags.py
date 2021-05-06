def tags(tag):
    def decorator(fn):
        def wrapper(*args,**kwargs):
            return f"<{tag}>{fn(*args)}</{tag}>"
        return wrapper
    return decorator

@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
