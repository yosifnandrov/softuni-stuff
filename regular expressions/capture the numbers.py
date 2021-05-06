import re

line = input()
pattern = r"\d+"

only_nums = []
while line:
    found_nums = re.findall(pattern,line)
    if found_nums:
        only_nums.extend(found_nums)
    line = input()
print(" ".join(only_nums))





