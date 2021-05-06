text = input().lower()

total_sum = 0

searched_words = ["sand","water","fish","sun"]

for word in searched_words:
    if word in text:
        total_sum += text.count(word)
print(total_sum)
