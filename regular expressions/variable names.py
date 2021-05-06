import re

text = input()

pattern = r"(^_|(?<=\s_))[a-zA-Z0-9]+((?=[\s.])|$)"

result = re.finditer(pattern, text)
found = []
for res in result:
    found.append(res.group())

print(",".join(found))