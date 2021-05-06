text = input().split()
text = "".join(text)
my_dict = {}
for letter in text:
    if letter not in my_dict:
        my_dict[letter] = 0
        my_dict[letter] += (text.count(letter))

for key, value in my_dict.items():
    print(f"{key} -> {value}")



