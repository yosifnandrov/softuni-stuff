data_type = input()
data = input()


def data_int(some_int):
    return some_int*2


def data_float(some_flaot):
    return f"{some_flaot*1.5:.2f}"

def data_string(some_string):
    some_string = "$" + some_string + "$"
    return some_string

if data_type == "int":
    data = int(data)
    print(data_int(data))
elif data_type == "real":
    data = float(data)
    print(data_float(data))
elif data_type == "string":
    print(data_string(data))
