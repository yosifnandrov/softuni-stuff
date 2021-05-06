some_text = input()

for letter in some_text:
    while letter*2 in some_text:
        new_text = some_text.replace(letter*2, letter)
        some_text = new_text
print(some_text)