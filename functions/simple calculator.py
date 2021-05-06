operator = input()
number_1 = int(input())
number_2 = int(input())

def solve(number_1 , number_2, operator):
    if operator == "multiply":
        return number_1 * number_2
    elif operator == "divide":
        return number_1 / number_2
    elif operator == "subtract":
        return number_1 - number_2
    elif operator == "add":
        return number_1 + number_2
result = int(solve(number_1, number_2, operator))
print(result)