import re


with open("names.txt", "w") as file:
    for i in range(11):
        file.write(f'{i}hello world\n')

with open("names.txt", "r+") as file_again:
    a = "\n".join(file_again.readlines())
    my_lines = a.split('\n\n')
    for row in my_lines:
        file_again.write(f'{row}\n')

with open("names.txt", "r+") as file:
    text = file.read()
    print(text)
    pattern = r"(world)"
    matches = re.findall(pattern,text)
    for word in matches:
        text = text.replace(word, "kopele")
    with open("names.txt", "w") as new_file:
        new_file.write(text)
