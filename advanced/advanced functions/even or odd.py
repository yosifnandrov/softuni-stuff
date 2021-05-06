def even_odd(*args):
    command = args[-1]
    args = args[:len(args)-1]
    if command == "odd":
        odd = [el for el in args if el % 2 == 1]
        return odd
    elif command == "even":
        even = [el for el in args if el % 2 == 0]
        return even


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
