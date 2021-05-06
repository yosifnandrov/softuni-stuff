# import re
#
# text = "kvo stava maina"
#
# word = re.findall(r'\w+', text)
#
# for w in word:
#     print(w)

# n = input()
# is_bigger = True
# while is_bigger:
#     sum_digits = 0
#     for num in n:
#         sum_digits += int(num)
#     if sum_digits > 9:
#         n = str(sum_digits)
#     else:
#         n = str(sum_digits)
#         is_bigger = False
# print(n)

# some_text = "2i1iabv.ahghth.hkywu.2dadfsd".split(".")
# some_text[2] = some_text[2][2::]
# print(some_text[2])


# import string
#
# word = "A"
# word = word.lower()
# a = string.ascii_lowercase.index(word)
# print(a)


# opit = "b2353u"
#
# number = opit[1:-1]
# print(number)


number = input()
sorted_numbers = []
for n in number:
    sorted_numbers.append(n)
a = "".join(reversed(sorted(sorted_numbers)))
print(a)



