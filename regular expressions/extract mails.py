import re

text = input()

pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[-\._]?[a-zA-Z0-9]+@[a-z]+[\-\.]?[a-z]+[\-\.]?[a-z]+\.[a-z]+(\s|(?=$))?"

result = re.finditer(pattern,text)

for res in result:
    print(res.group())