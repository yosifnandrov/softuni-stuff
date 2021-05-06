first_number = int(input())
second_number = int(input())

def factorial_division(first_number, second_number):
    multiplyer = 1
    multiplyer_two = 1
    for n in range(first_number, 0, -1):
        multiplyer = n * multiplyer
    for i in range(second_number, 0, -1):
        multiplyer_two = i * multiplyer_two
    result = multiplyer / multiplyer_two
    print(f"{result:.2f}")


factorial_division(first_number, second_number)

