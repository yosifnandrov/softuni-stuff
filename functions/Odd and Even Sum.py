number = int(input())

def odd_even_sum(number):
    number = str(number)
    even = 0
    odd = 0
    for n in number:
        n = int(n)
        if n % 2 == 0:
            even += n
        else:
            odd += n
    print(f"Odd sum = {odd}, Even sum = {even}")
odd_even_sum(number)