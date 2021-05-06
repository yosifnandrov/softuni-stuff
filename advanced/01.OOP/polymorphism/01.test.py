my_list = ["1","2","dog","4"]


if all([el.isdigit() for el in my_list]):
    print("DIGITS!")
else:
    print("NOPE!")

execute = lambda fn,*args: fn(*args)

def say_hi():
    return "hello"


print(execute(say_hi))