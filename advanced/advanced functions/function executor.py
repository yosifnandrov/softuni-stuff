def func_executor(*args):
    my_list = []
    for arg in args:
        a,b = arg
        my_list.append(a(*b))
    return my_list

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))