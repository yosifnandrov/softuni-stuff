# year = int(input())
# text = str(year + 1)
# not_happy = True
# same = 0
# while not_happy:
#     for letter in text:
#         same = 0
#         for second_letter in text:
#             if letter == second_letter:
#                 same += 1
#         if same > 1:
#             not_happy = True
#             text = str(int(text) + 1)
#             break
#         else:
#             not_happy = False
# print(text)


year = int(input()) + 1

while True:
    is_happy = True
    year_as_string = str(year)
    for index_1 in range(len(year_as_string)):
        for index_2 in range(len(year_as_string)):
            if index_1 == index_2:
                continue
            if year_as_string[index_1] == year_as_string[index_2]:
                is_happy = False
                break
    if is_happy:
        print(year)
        break
    else:
        year += 1



