numbers = input().split(", ")
numbers = [int(el) for el in numbers]
def func(some_list):
    i = 10
    l = 0
    while i <= max(some_list) + 9:
        new_list = []
        for x in some_list:
            x = int(x)
            if l < x <= i:
                new_list.append(x)
            else:
                continue
        print(f"Group of {i}'s: {new_list}")
        i += 10
        l += 10
func(numbers)


