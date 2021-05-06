def cache(fn):
    log = {}
    def wrapper(*args,**kwargs):
        if args not in log:
            result = fn(*args,**kwargs)
            log[args[0]] = result
            return result
        return log[args]
    wrapper.log = log
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))