import re
cool_threshold = 1
text = input()
matches_list = []
final_list = []
pattern = r"(?P<name>([*]{2})[A-Z][a-z]{2,}([*]{2})|([:]{2})[A-Z][a-z]{2,}([:]{2}))"
matches = re.finditer(pattern, text)
for match in matches:
    matches_list.append(match.group("name"))

pattern_numbers = r"\d"
matches_numbers = re.findall(pattern_numbers,text)
matches_numbers = [int(el) for el in matches_numbers]
for i in range(len(matches_numbers)):
    cool_threshold *= matches_numbers[i]
print(f"Cool threshold: {cool_threshold}")


for word in matches_list:
    word_threshold = 0
    for letter in word:
        if letter.isalpha():
            word_threshold += ord(letter)
    if word_threshold >= cool_threshold:
        final_list.append(word)

print(f"{len(matches_list)} emojis found in the text. The cool ones are:")
for cool in final_list:
    print(cool)

