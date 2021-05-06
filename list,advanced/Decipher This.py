print("Hello, you can give me a coded message that starts with number and random word behind it and i can try to decipher it")
message = input("Give me your message to decipher").split()
def decipher_this(some_text):
    digits = ""
    for letter in range(len(some_text)):
        some_text = list(some_text)
        if some_text[letter].isdigit():
            digits += some_text[letter]
        else:
            some_text[letter], some_text[-1] = some_text[-1], some_text[letter]
            break
    digits = int(digits)
    some_text = [i for i in some_text if not i.isdigit()]
    some_text_str = "".join(some_text)
    print(f"{chr(digits)}{some_text_str}", end=" ")
for word in message:
    decipher_this(word)





