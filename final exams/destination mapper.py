import re

text = input()

pattern = r"(=|\/)(?P<word>[A-Z][A-Za-z]{2,})(\1)"
new_list = []
matches = re.finditer(pattern,text)
len_dist = 0
for match in matches:
    new_list.append(match.group("word"))
if new_list:
    print("Destinations:", end=" ")
    for i in range(len(new_list)):
        len_dist += len(new_list[i])
    print(f"{', '.join(new_list)}")
else:
    print("Destinations:")

print(f"Travel Points: {len_dist}")



