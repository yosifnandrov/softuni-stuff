some_text = input()


for i in range(len(some_text)):
    if some_text[i] == ":":
        print(f"{some_text[i]}{some_text[i+1]}")