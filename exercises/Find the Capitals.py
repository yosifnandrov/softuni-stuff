text = input()

new_list = []
for i in range(len(text)):
    if text[i].isupper():
        new_list.append(i)
print(new_list)