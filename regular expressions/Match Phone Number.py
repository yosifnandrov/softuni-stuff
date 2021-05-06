import re

telephone_numbers = input()
pattern = r"(\+359\s2\s\d{3}\s\d{4}\b)|(\+359\-2\-\d{3}\-\d{4}\b)"

phone = re.finditer(pattern,telephone_numbers)
new_list = []
for p in phone:
    new_list.append(p.group(0))

print(", ".join(new_list))