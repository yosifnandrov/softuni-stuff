number = int(input())
count_open = 0
count_closed = 0
for _ in range(number):
    text = input()
    if "(" == text:
        count_open += text.count("(")
    if ")" == text:
        count_closed += text.count(")")


if count_open == count_closed:
    if count_open == 0:
        print("UNBALANCED")
    else:
        print("BALANCED")
else:
    print("UNBALANCED")


