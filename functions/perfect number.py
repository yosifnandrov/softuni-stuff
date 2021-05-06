number = int(input())

def is_number_perfect(number):
    sum_n = 0
    for n in range(1, number):
        if number % n == 0:
            sum_n += n
    if sum_n == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

is_number_perfect(number)