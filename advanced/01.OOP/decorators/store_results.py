class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open("results.txt","a") as f:
            res = self.func(*args,**kwargs)
            f.write(f"Function {self.func.__name__} was called. Result: {res}\n")


@store_results
def mul(a,b):
    return a * b


mul(6,4)
mul(6,4)
mul(6,4)



with open("results.txt","r") as f:
    print(f.readlines())