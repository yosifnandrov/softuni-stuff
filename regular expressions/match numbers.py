import re

all_numbers = input()

pattern = r"(^|(?<=\s))[-]?\d+(\.\d+)?($|(?=\s))"
new_list = []
found_numbers = re.finditer(pattern,all_numbers)

for n in found_numbers:
    new_list.append(n.group())

print(' '.join(new_list))