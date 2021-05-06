def get_primes(some_list):
    for num in some_list:
        counter = 0
        for i in range(1,int(num)):
            if int(num) % i == 0:
                counter += 1
        if counter == 1:
            yield num


print(list(get_primes(range(100))))