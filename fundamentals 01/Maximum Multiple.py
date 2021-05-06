# import sys
# divisor = int(input())
# bound = int(input())
# max_num = -sys.maxsize
# for number in range(1, bound + 1):
#     if number % divisor == 0:
#         if number > max_num:
#             max_num = number
# print(max_num)

divisor = int(input())
bound = int(input())
for number in range(bound, 0, -1):
    if number % divisor == 0:
        print(number)
        break
