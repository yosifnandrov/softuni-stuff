# data = input().split()
# data = [int(x) for x in data]
#
# print(max(data))

# twice = lambda x: x * x
# d = twice(5)
# print(d)

# nums = [int(el) for el in input().split()]
# evan = [n for n in nums if n % 2 == 0]
# print(max(evan))
number = input("Give me a number and i will give you it's binary!\n")
while True:
    for digits in number:
        if digits.isalpha():
            print(f"Not valid input\n")
            break
    else:
        number = int(number)
        number = (bin(number).replace("0b", ""))
        print(number)
    number = input("Give me a number and i will give you it's binary!\n")