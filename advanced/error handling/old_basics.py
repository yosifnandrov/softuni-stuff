#for index, digit in enumerate(n_to_text):

n = int(input())
for i in range(1111, 10000):
    i = str(i)
    for num in i:
        if "0" in i:
            continue
        else:
            if all([n%int(num) == 0 for num in i]):
                print(int(i), end=" ")
                break
