single_string = input()
digits = ""
letters = ""
symbols = ""

for word in single_string:
    if word.isdigit():
        digits += word
    elif word.isalpha():
        letters += word
    else:
        symbols += word
print(f"{digits}\n{letters}\n{symbols}")