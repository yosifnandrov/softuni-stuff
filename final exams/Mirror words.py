import re
new_list = []
text = input()
pattern = r"(@|#)(?P<word>[a-zA-Z]{3,})(\1)(?=\1(?P<word_two>[a-zA-Z]{3,})\1)"
matches = re.finditer(pattern, text)

for match in matches:
    new_list.append(match.group("word"))
    new_list.append(match.group("word_two"))
if len(new_list) == 0:
    print(f"No word pairs found!")
else:
    print(f"{len(new_list)//2} word pairs found!")
mirror_words = []
for i in range(0,len(new_list),2):
    if new_list[i] == new_list[i+1][::-1]:
        mirror_words.append(new_list[i])
        mirror_words.append(new_list[i+1])
if not mirror_words:
    print(f"No mirror words!")
else:
    print("The mirror words are:")
    for index in range(0,len(mirror_words),2):
        if index == len(mirror_words) - 2:
            print(f"{mirror_words[index]} <=> {mirror_words[index+1]}")
        else:
            print(f"{mirror_words[index]} <=> {mirror_words[index+1]}", end=", ")




