n = int(input())
word = input()
all_words = []
searched_word = []
counter = 0
for _ in range(n):
    current_word = input()
    all_words.append(current_word)
    if word in current_word:
        searched_word.append(current_word)
print(all_words)
print(searched_word)

